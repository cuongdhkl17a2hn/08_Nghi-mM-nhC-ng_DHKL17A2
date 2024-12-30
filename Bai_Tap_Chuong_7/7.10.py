import tkinter as tk
from tkinter import messagebox

# Hàm để hiển thị thông báo chào hỏi và tuổi
def hien_thi_thong_bao():
    try:
        # Lấy tên và tuổi từ các ô nhập liệu
        ten = entry_ten.get()
        tuoi = int(entry_tuoi.get())
        
        # Xác định thông điệp về độ tuổi
        if tuoi >= 18:
            tuoi_message = f"Bạn đã trưởng thành! {tuoi} tuổi."
        else:
            tuoi_message = f"Bạn còn nhỏ tuổi! {tuoi} tuổi."
        
        # Hiển thị thông báo
        messagebox.showinfo("Thông Báo", f"Xin chào {ten}.\n{tuoi_message}")
    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tuổi hợp lệ!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chương Trình Chào Hỏi")

# Tạo nhãn và ô nhập liệu cho tên
label_ten = tk.Label(root, text="Nhập tên của bạn:")
label_ten.pack(pady=5)
entry_ten = tk.Entry(root)
entry_ten.pack(pady=5)

# Tạo nhãn và ô nhập liệu cho tuổi
label_tuoi = tk.Label(root, text="Nhập tuổi của bạn:")
label_tuoi.pack(pady=5)
entry_tuoi = tk.Entry(root)
entry_tuoi.pack(pady=5)

# Tạo nút để hiển thị thông báo
button = tk.Button(root, text="Hiển thị thông báo", command=hien_thi_thong_bao)
button.pack(pady=10)

# Chạy chương trình Tkinter
root.mainloop()