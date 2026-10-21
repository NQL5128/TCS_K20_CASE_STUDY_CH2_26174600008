# Bài 6: Chương trình tương tác hoàn chỉnh
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất W: "))
so_phut = float(input("Nhập số phút: "))
don_gia = float(input("Nhập đơn giá: "))

# Tính toán điện năng và chi phí
dien_nang = (cong_suat * so_phut) / (60 * 1000)
chi_phi = dien_nang * don_gia

# In kết quả theo đúng định dạng mẫu của cô
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang}")
print(f"Chi phí: {chi_phi}")