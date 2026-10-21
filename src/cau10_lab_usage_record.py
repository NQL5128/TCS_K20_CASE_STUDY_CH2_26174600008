from datetime import datetime

# Nhập các thông tin theo yêu cầu
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất W: "))
so_phut = float(input("Nhập thời gian sử dụng (phút): "))
don_gia = float(input("Nhập đơn giá (VND/kWh): "))

# Tự tính toán điện năng, chi phí, giá trị Boolean và thời điểm ghi nhận
dien_nang = (cong_suat * so_phut) / (60 * 1000)
chi_phi = dien_nang * don_gia
tren_60_phut = so_phut > 60  # Trả về True/False không dùng if
thoi_diem_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Xuất kết quả theo đúng định dạng mẫu
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat:.2f} W")
print(f"Thời lượng: {int(so_phut)} phút")
print(f"Điện năng: {dien_nang:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_hien_tai}")