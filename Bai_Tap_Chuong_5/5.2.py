import sqlite3

# Kết nối tới cơ sở dữ liệu trong bộ nhớ
ket_noi = sqlite3.connect(":memory:")

print("Kết nối thành công tới cơ sở dữ liệu trong bộ nhớ!")

# Đóng kết nối
ket_noi.close()