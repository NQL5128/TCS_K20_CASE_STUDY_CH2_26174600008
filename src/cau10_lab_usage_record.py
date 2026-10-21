from datetime import datetime

# Nhập các thông tin theo yêu cầu
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất W: "))
so_phut = float(input("Nhập thời gian sử dụng (phút): "))
don_gia = float(input("Nhập đơn giá (VND/kWh): "))

# Tự tính toán điện năng, chi phí, thuế VAT, giá trị Boolean và thời điểm ghi nhận
dien_nang = (cong_suat * so_phut) / (60 * 1000)
chi_phi = dien_nang * don_gia
tong_tien_vat = chi_phi * 1.1  # Bổ sung tính thêm 10% thuế VAT (thay đổi có ý nghĩa cho phiên bản 2)
tren_60_phut = so_phut > 60  # Trả về True/False không dùng if
thoi_diem_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Xuất kết quả theo đúng định dạng mẫu
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat:.2f} W")
print(f"Thời lượng: {int(so_phut)} phút")
print(f"Điện năng: {dien_nang:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Tổng tiền (gồm VAT): {tong_tien_vat:.2f} VND")  # Xuất thêm trường dữ liệu VAT
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_hien_tai}")