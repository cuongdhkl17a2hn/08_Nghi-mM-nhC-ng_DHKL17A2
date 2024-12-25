import sqlite3

# Kết nối tới cơ sở dữ liệu
ket_noi = sqlite3.connect("test.db")
con_tror = ket_noi.cursor()

# Xóa một hàng cụ thể
con_tror.execute("DELETE FROM sinh_vien WHERE id = 1")

print("Xóa hàng thành công!")

# Đóng kết nối
ket_noi.commit()
con_tror.close()
ket_noi.close()