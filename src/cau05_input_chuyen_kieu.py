# 17. Nhập 4 giá trị và in type() ngay sau khi nhập
ma_may = input("Nhập mã máy: ")
print(type(ma_may))

cong_suat_raw = input("Nhập công suất W: ")
print(type(cong_suat_raw))

so_phut_raw = input("Nhập số phút: ")
print(type(so_phut_raw))

don_gia_raw = input("Nhập đơn giá: ")
print(type(don_gia_raw))

# 18. Chuyển đổi kiểu dữ liệu
cong_suat = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia = float(don_gia_raw)

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang = (cong_suat * so_phut) / (60 * 1000)
chi_phi = dien_nang * don_gia

# In kết quả ra màn hình
print("Điện năng:", dien_nang)
print("Chi phí:", chi_phi)