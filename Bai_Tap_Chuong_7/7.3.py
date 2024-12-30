import tkinter as tk

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Chương trình GUI với Phông chữ")

# Tạo nhãn với kiểu phông chữ thay đổi
nhan = tk.Label(cua_so, text="Phông chữ tùy chỉnh", font=("Arial", 16, "bold"))
nhan.pack()

# Chạy vòng lặp sự kiện
cua_so.mainloop()