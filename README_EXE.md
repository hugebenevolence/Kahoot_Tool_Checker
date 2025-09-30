# 🎯 Kahoot Quiz Viewer - Executable Files

## 📁 Các file exe đã tạo

### 🖥️ **KahootQuizViewer.exe** (Phiên bản chính)
- **Mô tả**: Ứng dụng chính không hiển thị console
- **Kích thước**: ~35MB (bao gồm tất cả dependencies)
- **Cách sử dụng**: Double-click để chạy
- **Đặc điểm**: 
  - Giao diện đẹp, không có cửa sổ console
  - Thích hợp cho người dùng cuối
  - Chạy hoàn toàn độc lập, không cần cài Python

### 🐛 **KahootQuizViewer_Debug.exe** (Phiên bản debug)
- **Mô tả**: Phiên bản có console để debug
- **Kích thước**: ~35MB 
- **Cách sử dụng**: Double-click để chạy
- **Đặc điểm**:
  - Hiển thị console với thông tin debug
  - Thích hợp khi gặp lỗi cần kiểm tra
  - Có thể xem error messages chi tiết

## 🚀 Cách sử dụng

1. **Chạy ứng dụng**:
   - Tìm file `KahootQuizViewer.exe` trong thư mục `dist/`
   - Double-click để chạy
   - Không cần cài đặt Python hay bất kỳ thứ gì khác!

2. **Nhập dữ liệu**:
   - **Quiz ID**: Dạng UUID (vd: f47ac10b-58cc-4372-a567-0e02b2c3d479)
   - **Game PIN**: 6-7 chữ số (vd: 735 0114, 7350114)

3. **Xem kết quả**:
   - Câu hỏi và đáp án sẽ hiển thị ngay trong ứng dụng
   - Giao diện đẹp mắt với theme dark

## ⚠️ Lưu ý quan trọng

- **Game PIN**: Chỉ hoạt động khi game Kahoot đang diễn ra
- **Quiz ID**: Luôn hoạt động (nếu quiz công khai)
- **Kết nối Internet**: Cần có internet để lấy dữ liệu từ Kahoot
- **Tường lửa**: Có thể cần cho phép ứng dụng truy cập internet

## 📂 Cấu trúc thư mục

```
extension/
├── dist/
│   ├── KahootQuizViewer.exe          # ← Chạy file này
│   └── KahootQuizViewer_Debug.exe    # ← Debug version
├── build/                            # Thư mục tạm (có thể xóa)
├── main.py                          # Source code gốc
├── kahoot_api.py                    # API handler
└── run.bat                          # Batch file backup
```

## 🔧 Troubleshooting

### Nếu gặp lỗi:
1. Thử chạy `KahootQuizViewer_Debug.exe` để xem lỗi chi tiết
2. Kiểm tra kết nối internet
3. Với Game PIN: Đảm bảo game đang active
4. Với Quiz ID: Đảm bảo quiz có quyền public

### Nếu file exe không chạy:
1. Kiểm tra antivirus (có thể chặn file)
2. Chạy với quyền administrator
3. Đảm bảo Windows đã cập nhật

## 💡 Tips

- **Chia sẻ**: Có thể copy file exe sang máy khác mà không cần cài Python
- **Backup**: Giữ lại source code (`main.py`, `kahoot_api.py`) để chỉnh sửa sau
- **Update**: Khi có cập nhật, chạy lại `pyinstaller` để tạo exe mới

---

**Tạo bởi**: Kitty-Tools Extension  
**Ngày tạo**: September 30, 2025  
**PyInstaller**: v6.16.0