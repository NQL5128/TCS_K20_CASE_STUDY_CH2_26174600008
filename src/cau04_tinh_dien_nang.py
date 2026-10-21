cong_suat_w = 250
so_phut = 60
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Dien nang tieu thu:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phi dien:", chi_phi, type(chi_phi))