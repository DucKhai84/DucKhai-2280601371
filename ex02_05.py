so_gio_lam = float(input("Số giờ làm: "))

luong_gio = float(input("Lương giờ: "))

gio_tieu_chuan = 44

gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

print("Số tiền thực lĩnh: ", gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5)