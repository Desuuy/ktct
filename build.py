"""Build index.html from src/ (template + question data + notes).

Usage:  python build.py
"""
from pathlib import Path

root = Path(__file__).parent
src = root / "src"
template = (src / "template.html").read_text(encoding="utf-8")
data = (
    (src / "data.js").read_text(encoding="utf-8")
    + "\n"
    + (src / "notes.js").read_text(encoding="utf-8")
    + "\nCHAPTERS.forEach(c=>{c.notes=NOTES[c.id];if(EXTRA[c.id])c.qs=c.qs.concat(EXTRA[c.id]);if(EXTRA2[c.id])c.qs=c.qs.concat(EXTRA2[c.id]);if(EXTRA3[c.id])c.qs=c.qs.concat(EXTRA3[c.id]);});"
)
(root / "index.html").write_text(template.replace("__DATA__", data), encoding="utf-8")
print("Built index.html")
