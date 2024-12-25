import sqlite3

# Kết nối tới cơ sở dữ liệu
ket_noi = sqlite3.connect("test.db")
con_tror = ket_noi.cursor()

# Tạo bảng
con_tror.execute("""
    CREATE TABLE IF NOT EXISTS sinh_vien (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten TEXT NOT NULL,
        tuoi INTEGER,
        lop TEXT
    )
""")
print("Tạo bảng thành công!")

# Đóng kết nối
con_tror.close()
ket_noi.close()