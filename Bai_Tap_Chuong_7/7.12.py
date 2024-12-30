import tkinter as tk
from tkinter import messagebox

# Hàm tính chỉ số BMI và hiển thị kết quả
def tinh_bmi():
    try:
        # Lấy cân nặng và chiều cao từ các ô nhập liệu
        can_nang = float(entry_can_nang.get())
        chieu_cao = float(entry_chieu_cao.get())

        # Kiểm tra nếu chiều cao và cân nặng hợp lệ
        if can_nang <= 0 or chieu_cao <= 0:
            messagebox.showerror("Lỗi", "Cân nặng và chiều cao phải là số dương!")
            return

        # Tính chỉ số BMI
        bmi = can_nang / (chieu_cao ** 2)

        # Hiển thị kết quả BMI
        entry_bmi.delete(0, tk.END)
        entry_bmi.insert(0, f"{bmi:.2f}")
        
        # Kết luận về BMI
        if bmi < 18.5:
            ket_luan = "Thiếu cân"
        elif 18.5 <= bmi < 24.9:
            ket_luan = "Bình thường"
        elif 25 <= bmi < 29.9:
            ket_luan = "Thừa cân"
        else:
            ket_luan = "Béo phì"

        # Hiển thị kết luận về BMI
        messagebox.showinfo("Kết luận BMI", f"Chỉ số BMI là: {bmi:.2f}\nKết luận: {ket_luan}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập các giá trị hợp lệ cho cân nặng và chiều cao.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính Chỉ Số BMI")

# Tạo nhãn và ô nhập liệu cho cân nặng
label_can_nang = tk.Label(root, text="Nhập cân nặng (kg):")
label_can_nang.pack(pady=5)
entry_can_nang = tk.Entry(root)
entry_can_nang.pack(pady=5)

# Tạo nhãn và ô nhập liệu cho chiều cao
label_chieu_cao = tk.Label(root, text="Nhập chiều cao (m):")
label_chieu_cao.pack(pady=5)
entry_chieu_cao = tk.Entry(root)
entry_chieu_cao.pack(pady=5)

# Tạo ô hiển thị kết quả BMI
label_bmi = tk.Label(root, text="Chỉ số BMI:")
label_bmi.pack(pady=5)
entry_bmi = tk.Entry(root, state='readonly')
entry_bmi.pack(pady=5)

# Tạo nút tính BMI
button_tinh_bmi = tk.Button(root, text="Tính BMI", command=tinh_bmi)
button_tinh_bmi.pack(pady=10)

# Chạy chương trình Tkinter
root.mainloop()