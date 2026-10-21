tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60

su_dung_lau = tong_phut > 60

du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0

print("Tong so phut:", tong_phut)
print("So gio tron:", so_gio)
print("So phut con lai:", so_phut_con_lai)
print("Su dung lau:", su_dung_lau)
print("Du lieu hop le:", du_lieu_hop_le)

print("Bieu thuc 1:", 100 + 20 * 3)
print("Bieu thuc 2:", (100 + 20) * 3)