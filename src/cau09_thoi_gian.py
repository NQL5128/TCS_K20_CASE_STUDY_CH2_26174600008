from datetime import datetime

# Lấy mốc thời điểm hiện tại
thoi_diem = datetime.now()
# Định dạng thời gian thành dạng chữ (chuỗi)
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Phần bổ sung tính khoảng thời gian (timedelta)
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# === TRẢ LỜI CÂU HỎI TRONG ĐỀ ===
# 24. Dự đoán kết quả phép trừ: Kết quả khoảng thời gian là 1 giờ 50 phút (1:50:00).
# 25. Giải thích sự khác nhau:
# - datetime: Kiểu dữ liệu biểu diễn một mốc thời gian cụ thể (gồm năm, tháng, ngày, giờ, phút, giây).
# - str: Kiểu chuỗi văn bản (dùng để hiển thị hoặc lưu trữ dưới dạng text thông thường sau khi định dạng).
# - timedelta: Kiểu dữ liệu biểu diễn một khoảng thời gian (độ lệch thời gian, là kết quả của phép trừ giữa hai mốc datetime).