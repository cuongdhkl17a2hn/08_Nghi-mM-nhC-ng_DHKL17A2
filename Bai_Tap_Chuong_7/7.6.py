import tkinter as tk

# Hàm xử lý khi nhấn nút "Validate"
def tra_nguoc_chuoi():
    chuoi_nhap = o_nhap.get()
    chuoi_nguoc = chuoi_nhap[::-1]
    nhan_ket_qua.config(text=f"! {chuoi_nguoc}")

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Chương trình trả ngược chuỗi")

# Tạo nhãn và ô nhập
nhan_huong_dan = tk.Label(cua_so, text="Enter a word:")
nhan_huong_dan.pack()

o_nhap = tk.Entry(cua_so, width=30)
o_nhap.pack()

# Tạo nút "Validate"
nut_validate = tk.Button(cua_so, text="Validate", command=tra_nguoc_chuoi)
nut_validate.pack()

# Tạo nhãn để hiển thị kết quả
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

# Chạy vòng lặp sự kiện
cua_so.mainloop()