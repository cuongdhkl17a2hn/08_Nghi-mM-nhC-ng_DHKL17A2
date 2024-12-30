import tkinter as tk
from tkinter import messagebox
import math

# Hàm tính GCD (Ước Số Chung Lớn Nhất)
def tinh_gcd():
    try:
        # Lấy hai số nguyên từ ô nhập liệu
        a = int(entry_a.get())
        b = int(entry_b.get())

        # Tính GCD của a và b
        gcd = math.gcd(a, b)
        
        # Hiển thị kết quả GCD
        messagebox.showinfo("Kết quả GCD", f"GCD của {a} và {b} là: {gcd}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ.")

# Hàm tính LCM (Bội Số Chung Nhỏ Nhất)
def tinh_lcm():
    try:
        # Lấy hai số nguyên từ ô nhập liệu
        a = int(entry_a.get())
        b = int(entry_b.get())

        # Tính LCM của a và b
        if a == 0 or b == 0:
            messagebox.showerror("Lỗi", "LCM không xác định khi một trong hai số bằng 0.")
            return
        lcm = abs(a * b) // math.gcd(a, b)
        
        # Hiển thị kết quả LCM
        messagebox.showinfo("Kết quả LCM", f"LCM của {a} và {b} là: {lcm}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính GCD và LCM")

# Tạo nhãn hướng dẫn cho hai số
label_a = tk.Label(root, text="Nhập số nguyên a:")
label_a.pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Nhập số nguyên b:")
label_b.pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack(pady=5)

# Tạo nút tính GCD và LCM
button_gcd = tk.Button(root, text="Tính GCD", command=tinh_gcd)
button_gcd.pack(pady=10)

button_lcm = tk.Button(root, text="Tính LCM", command=tinh_lcm)
button_lcm.pack(pady=10)

# Chạy chương trình Tkinter
root.mainloop()