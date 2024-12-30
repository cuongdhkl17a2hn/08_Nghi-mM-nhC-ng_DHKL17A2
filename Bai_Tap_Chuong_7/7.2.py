import tkinter as tk

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Chương trình GUI với Nhãn")

# Thêm nhãn vào cửa sổ
nhan = tk.Label(cua_so, text="Chào mừng bạn đến với GUI Python!")
nhan.pack()

# Chạy vòng lặp sự kiện
cua_so.mainloop()