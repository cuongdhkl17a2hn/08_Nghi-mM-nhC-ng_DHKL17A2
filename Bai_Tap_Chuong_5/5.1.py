import sqlite3

# Tạo và kết nối cơ sở dữ liệu
ket_noi = sqlite3.connect("test.db")

# In phiên bản SQLite
print(f"Phiên bản SQLite: {sqlite3.sqlite_version}")

# Đóng kết nối
ket_noi.close()