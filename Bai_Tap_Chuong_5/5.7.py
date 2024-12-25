import sqlite3

# Kết nối tới cơ sở dữ liệu
ket_noi = sqlite3.connect("test.db")
con_tror = ket_noi.cursor()

# Cập nhật giá trị trong cột
con_tror.execute("UPDATE sinh_vien SET lop = 'Công nghệ thông tin' WHERE lop = 'CNTT'")

print("Cập nhật giá trị thành công!")

# Đóng kết nối
ket_noi.commit()
con_tror.close()
ket_noi.close()