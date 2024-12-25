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

# Chèn dữ liệu
con_tror.executemany("""
    INSERT INTO sinh_vien (ten, tuoi, lop) VALUES (?, ?, ?)
""", [
    ("Nguyễn Văn A", 20, "CNTT"),
    ("Trần Thị B", 21, "Kế toán"),
    ("Lê Văn C", 22, "Quản trị kinh doanh")
])

# Lấy tất cả các bản ghi
con_tror.execute("SELECT * FROM sinh_vien")
rows = con_tror.fetchall()

print("Các bản ghi trong bảng:")
for row in rows:
    print(row)

# Đóng kết nối
con_tror.close()
ket_noi.close()