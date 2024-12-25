import sqlite3

# Kết nối tới cơ sở dữ liệu
ket_noi = sqlite3.connect("test.db")
con_tror = ket_noi.cursor()

# Lấy danh sách các bảng
con_tror.execute("SELECT name FROM sqlite_master WHERE type='table';")
bangs = con_tror.fetchall()

print("Các bảng trong cơ sở dữ liệu:")
for bang in bangs:
    print(bang[0])

# Đóng kết nối
con_tror.close()
ket_noi.close()

