import sqlite3

# Kết nối tới cơ sở dữ liệu
ket_noi = sqlite3.connect("test.db")
con_tror = ket_noi.cursor()

# Đếm số bản ghi trong bảng
con_tror.execute("SELECT COUNT(*) FROM sinh_vien")
so_ban_ghi = con_tror.fetchone()[0]

print(f"Số lượng bản ghi trong bảng: {so_ban_ghi}")

# Đóng kết nối
con_tror.close()
ket_noi.close()