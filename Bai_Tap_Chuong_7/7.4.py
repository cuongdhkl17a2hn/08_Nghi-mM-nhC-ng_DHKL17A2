import tkinter as tk

def gui_thong_tin():
    print(f"Tên: {ten.get()}")
    print(f"ID: {id.get()}")
    print(f"Mật khẩu: {mat_khau.get()}")

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Thông tin Sinh viên")

# Tạo nhãn và hộp văn bản cho tên sinh viên
tk.Label(cua_so, text="Tên sinh viên:").grid(row=0, column=0, padx=10, pady=5)
ten = tk.Entry(cua_so)
ten.grid(row=0, column=1, padx=10, pady=5)

# Tạo nhãn và hộp văn bản cho ID sinh viên
tk.Label(cua_so, text="ID sinh viên:").grid(row=1, column=0, padx=10, pady=5)
id = tk.Entry(cua_so)
id.grid(row=1, column=1, padx=10, pady=5)

# Tạo nhãn và hộp văn bản cho mật khẩu
tk.Label(cua_so, text="Mật khẩu:").grid(row=2, column=0, padx=10, pady=5)
mat_khau = tk.Entry(cua_so, show="*")
mat_khau.grid(row=2, column=1, padx=10, pady=5)

# Tạo nút gửi
nut_gui = tk.Button(cua_so, text="Gửi", command=gui_thong_tin)
nut_gui.grid(row=3, column=1, pady=10)

# Chạy vòng lặp sự kiện
cua_so.mainloop()