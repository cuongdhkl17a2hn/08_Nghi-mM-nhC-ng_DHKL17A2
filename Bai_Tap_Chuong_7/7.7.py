import tkinter as tk

# Hàm tính tổng từ 1 đến N
def tinh_tong():
    try:
        # Lấy giá trị N từ ô nhập
        n = int(o_nhap.get())
        # Tính tổng
        tong = sum(range(1, n + 1))
        # Hiển thị kết quả
        nhan_ket_qua.config(text=f"Tổng từ 1 đến {n} là: {tong}")
    except ValueError:
        # Thông báo nếu người dùng nhập sai
        nhan_ket_qua.config(text="Vui lòng nhập một số nguyên hợp lệ!")

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Tính tổng 1 + 2 + ... + N")

# Tạo nhãn và ô nhập
nhan_huong_dan = tk.Label(cua_so, text="Nhập một số nguyên N:")
nhan_huong_dan.pack()

o_nhap = tk.Entry(cua_so, width=20)
o_nhap.pack()

# Tạo nút tính toán
nut_tinh_toan = tk.Button(cua_so, text="Tính tổng", command=tinh_tong)
nut_tinh_toan.pack()

# Tạo nhãn để hiển thị kết quả
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

# Chạy vòng lặp sự kiện
cua_so.mainloop()