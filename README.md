# Ôn thi Kinh tế chính trị Mác – Lênin

Trang web tĩnh để ôn thi môn KTCT Mác – Lênin. Nội dung bám theo *Giáo trình KTCT Mác – Lênin (dành cho bậc đại học hệ không chuyên lý luận chính trị)*, Bộ GD&ĐT, NXB Chính trị quốc gia Sự thật, 2021.

- 6 chương, mỗi chương học theo 3 bước: **Lý thuyết → Xem câu hỏi & đáp án → Làm bài** (có tính giờ, chấm điểm, giải thích, làm lại câu sai).
- **Phòng thi thử** 60 câu / 60 phút: mỗi chương lấy ngẫu nhiên 10 câu, hết giờ tự nộp bài.
- Tổng cộng 222 câu; thứ tự đáp án được xáo trộn mỗi lần làm.
- Không cần backend: một file `index.html` duy nhất, điểm cao nhất lưu trong `localStorage` của trình duyệt.

## Cấu trúc

```
index.html          # file đã build, đây là trang được host
build.py            # ghép src/ thành index.html
src/template.html   # giao diện + logic (HTML/CSS/JS)
src/data.js         # tiêu đề chương + ngân hàng câu hỏi gốc
src/notes.js        # lý thuyết từng chương (NOTES), câu hỏi bổ sung (EXTRA) và câu hỏi tham khảo Quizlet (EXTRA2)
```

Mỗi câu hỏi có dạng `["Câu hỏi", ["A", "B", "C", "D"], chỉ_số_đáp_án_đúng, "Giải thích", cố_định?]`. Phần tử thứ 5 (`1`) dùng cho câu không được xáo đáp án.

## Sửa nội dung

1. Sửa câu hỏi trong `src/data.js` hoặc `src/notes.js`, giao diện trong `src/template.html`.
2. Chạy `python build.py` để tạo lại `index.html`.
3. Commit và push.

## Deploy lên Vercel

Không cần build: `index.html` đã chứa đủ dữ liệu. `vercel.json` tắt bước build, `.vercelignore` chỉ đẩy trang web lên (không đẩy `src/`, `build.py`).

**Cách 1 – qua GitHub (khuyên dùng):** push repo lên GitHub → vào https://vercel.com/new → *Import* repo → Framework Preset để **Other** → bấm **Deploy**. Mỗi lần push lên `main`, Vercel tự deploy lại.

**Cách 2 – bằng CLI:**

```bash
npm i -g vercel
vercel          # lần đầu: đăng nhập, chọn scope, đặt tên project
vercel --prod   # deploy bản chính thức
```

## Host bằng GitHub Pages

```bash
git init
git add .
git commit -m "Trang ôn thi KTCT"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

Sau đó vào **Settings → Pages → Build and deployment**, chọn *Deploy from a branch*, branch `main`, thư mục `/ (root)`, rồi bấm Save. Khoảng 1 phút sau trang sẽ chạy ở `https://<username>.github.io/<repo>/`.

Mở chương trực tiếp bằng hash: `#chuong-1` … `#chuong-6`, phòng thi thử: `#thi-thu`.

## Nguồn và lưu ý

**Giáo trình (khung nội dung):** Bộ GD&ĐT, *Giáo trình Kinh tế chính trị Mác – Lênin (dành cho bậc đại học hệ không chuyên lý luận chính trị)*, NXB Chính trị quốc gia Sự thật, 2021 (PGS.TS Ngô Tuấn Nghĩa chủ biên). Chưa đọc được toàn văn bản in này.

**Văn bản đã đối chiếu toàn văn:** bản thảo giáo trình của Hội đồng biên soạn (PGS.TS Ngô Tuấn Nghĩa chủ trì), bản số hóa trên Internet Archive:
- https://archive.org/details/giao-trinh-kinh-te-chinh-tri-mac-lenin

**Xác nhận tên chương, mục:**
- Ma trận đề thi KTCT, Học viện Kỹ thuật Mật mã: https://ktdbcl.actvn.edu.vn/files/de-thi-mau/ma-tran-de-thi-kinh-te-chinh-tri.pdf
- Đề cương học phần ĐH Khoa học Huế: https://oj.husc.edu.vn/khoallct/downloads/2020/20200108141837_thong_tin_hoc_phan_ktct_moi.docx
- Đề cương học phần ĐH Sao Đỏ: https://saodo.edu.vn/uploads/about/ctdt2020-chung/ctri002.pdf

**Bộ đề tham khảo (Quizlet, do sinh viên soạn, không phải nguồn chính thức):** các câu có ghi chú "Dạng câu hỏi thường gặp trong các bộ đề ôn thi trên Quizlet" (mảng `EXTRA2`). Chỉ lấy câu mà nhiều bộ đề cho đáp án thống nhất; câu hỏi được viết lại. Ví dụ các bộ đề:
- https://quizlet.com/vn/821632556/kinh-te-chinh-tri-mac-lenin-c1-2-04-pts-flash-cards/
- https://quizlet.com/vn/828938113/kinh-te-chinh-tri-mac-lenin-c3-4-04-pts-flash-cards/
- https://quizlet.com/vn/840777037/kinh-te-chinh-tri-mac-lenin-c5-6-04-pts-flash-cards/
- https://quizlet.com/vn/850132191/chuong-6cong-nghiep-hoa-hien-dai-hoa-va-hoi-nhap-kinh-te-quoc-te-cua-viet-nam-flash-cards/

**Phần viết từ kiến thức chung, chưa đối chiếu nguyên văn:** một số định nghĩa và mô tả mở rộng trong phần lý thuyết (sức lao động, mô tả chi tiết các mức độ hội nhập, 3 mô hình công nghiệp hóa, định nghĩa CNH-HĐH của Hội nghị TW 7 khóa VII…). Khi có bản in 2021 nên dò lại.
# ktct
