import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi người dùng chọn một bài tập
def hien_thi_bai_tap(chuong, bai):
    tieude = f"Chương {chuong} - Bài {bai}"
    noidung = f"Nội dung: Giải phương trình bậc 2"
    messagebox.showinfo(tieude, noidung)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Hệ thống bài tập Python nâng cao")

# Tạo thanh menu
menu_bar = tk.Menu(root)

# Tạo menu cho các chương
for chuong in range(1, 8):
    chuong_menu = tk.Menu(menu_bar, tearoff=0)
    for bai in range(1, 10):
        bai_label = f"{chuong}.{bai}"
        chuong_menu.add_command(label=bai_label, command=lambda c=chuong, b=bai: hien_thi_bai_tap(c, b))
    menu_bar.add_cascade(label=f"Chương {chuong}", menu=chuong_menu)

# Gắn thanh menu vào cửa sổ chính
root.config(menu=menu_bar)

# Chạy ứng dụng
root.mainloop()