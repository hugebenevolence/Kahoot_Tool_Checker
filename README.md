# Kahoot Quiz Viewer Extension

Extension đơn giản để xem câu hỏi và đáp án từ Kahoot với giao diện đơn sắc, dễ sử dụng.

## Tính năng

- ✅ Giao diện đơn giản, màu đơn sắc (dark theme)
- ✅ Hỗ trợ nhập Quiz ID hoặc Game PIN
- ✅ Scroll để lướt xem các câu hỏi
- ✅ Hiển thị đầy đủ câu hỏi và đáp án
- ✅ Không có thành phần dư thừa
- ✅ Xử lý lỗi tốt
- ✅ Threading để tránh đơ giao diện

## Cài đặt và Sử dụng

### Yêu cầu
- Python 3.6+
- Tkinter (thường có sẵn với Python)
- Kết nối Internet

### Chạy Extension

1. Mở terminal/command prompt
2. Chuyển đến thư mục extension:
   ```bash
   cd extension
   ```
3. Chạy chương trình:
   ```bash
   python main.py
   ```

### Hướng dẫn sử dụng

1. **Nhập Quiz ID hoặc Game PIN**: 
   - **Quiz ID** (khuyên dùng): Chuỗi ký tự như "abc123-def456-ghi789"
     - Luôn hoạt động, không phụ thuộc vào trạng thái game
     - Tìm được trong URL của quiz trên Kahoot.it
   - **Game PIN**: Số 6-7 chữ số như "1234567" 
     - **CHỈ hoạt động khi game đang diễn ra**
     - Sau khi game kết thúc, PIN không còn valid

2. **Nhấn "Tải Quiz" hoặc Enter** để tải dữ liệu

3. **Xem kết quả**: 
   - Thông tin quiz hiển thị ở trên
   - Câu hỏi và đáp án hiển thị bên dưới
   - Sử dụng thanh scroll để lướt

### 💡 Lấy Quiz ID như thế nào?

1. Vào trang Kahoot.it
2. Tìm quiz bạn muốn xem
3. Trong URL sẽ có dạng: `https://create.kahoot.it/details/abc123-def456-ghi789`
4. Phần `abc123-def456-ghi789` chính là Quiz ID

## Cấu trúc File

```
extension/
├── main.py           # Giao diện chính (GUI)
├── kahoot_api.py     # Xử lý API Kahoot
└── README.md         # Hướng dẫn này
```

## Giao diện

- **Màu nền**: Xám đậm (#2c3e50)
- **Màu chữ**: Trắng (#ecf0f1)
- **Màu accent**: Xanh dương (#3498db)
- **Font**: Arial cho UI, Consolas cho kết quả
- **Layout**: Đơn giản, tập trung vào nội dung

## Xử lý lỗi

Extension xử lý các lỗi phổ biến:
- Quiz không tồn tại (404)
- Quiz private/restricted (403)
- Lỗi kết nối Internet
- Rate limiting
- SSL issues
- Định dạng input không hợp lệ

## Tính năng kỹ thuật

- **Threading**: Tải dữ liệu trong background thread
- **Rate Limiting**: Tránh bị block bởi Kahoot
- **SSL Handling**: Xử lý SSL certificates
- **Error Recovery**: Retry logic với exponential backoff
- **Clean Text**: Loại bỏ HTML tags và formatting

## Lưu ý

- Extension này chỉ dành cho mục đích giáo dục
- Tuân thủ Terms of Service của Kahoot
- Không spam requests
- Không sử dụng để gian lận trong thi cử

## Support

Nếu gặp lỗi, kiểm tra:
1. Kết nối Internet
2. Quiz ID/PIN đúng format
3. Quiz không phải private
4. Python version >= 3.6

## License

Phần mở rộng của Kitty-Tools project.
Chỉ sử dụng cho mục đích giáo dục và nghiên cứu.