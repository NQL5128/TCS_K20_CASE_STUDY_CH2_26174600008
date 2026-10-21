ma_may = input("Nhập mã máy: ")
# Sửa lỗi 1: Ép kiểu dữ liệu sang float để tính toán (tránh lỗi nhân chuỗi/TypeError)
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
# Sửa lỗi 2: Sửa tên biến thành dien_nang_kwh và sửa định dạng f-string từ :..3f thành :.3f
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Mô tả các lỗi đã phát hiện:
# - Lỗi 1: Biến cong_suat_w ban đầu nhận giá trị từ input() là kiểu chuỗi (str), khi đưa vào phép tính toán sẽ gây lỗi. Cần dùng float() để chuyển đổi.
# - Lỗi 2: Cú pháp f-string bị viết sai dấu chấm thừa (:..3f) và gọi nhầm tên biến tính toán. Cần sửa thành {dien_nang_kwh:.3f}.