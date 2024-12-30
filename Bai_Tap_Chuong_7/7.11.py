import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Hàm chuyển đổi năm Dương lịch sang năm Âm lịch và con giáp tương ứng
def convert_to_am_lich():
    try:
        # Lấy năm Dương lịch từ ô nhập liệu
        nam_duong_lich = int(entry_nam.get())
        
        # Tính năm Âm lịch (công thức đơn giản, cần điều chỉnh cho chính xác)
        nam_am_lich = nam_duong_lich - 1900 + 1
        con_giap_index = nam_am_lich % 12
        
        # Danh sách các con giáp tương ứng
        con_giap_list = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        
        # Lấy con giáp và tên
        con_giap = con_giap_list[con_giap_index]
        
        # Đường dẫn đến hình ảnh của con giáp
        image_path = f"images/{con_giap}.jpg"
        
        # Hiển thị kết quả
        messagebox.showinfo("Kết quả chuyển đổi", f"Năm {nam_duong_lich} Dương lịch tương ứng với năm {nam_am_lich} Âm lịch.\nCon giáp: {con_giap}")
        
        # Mở và hiển thị hình ảnh con giáp
        img = Image.open(image_path)
        img = img.resize((200, 200))  # Thay đổi kích thước hình ảnh nếu cần
        img_tk = ImageTk.PhotoImage(img)
        
        # Hiển thị hình ảnh trong cửa sổ Tkinter
        label_img.config(image=img_tk)
        label_img.image = img_tk  # Cần giữ tham chiếu để hình ảnh không bị mất

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một năm hợp lệ!")
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy hình ảnh của con giáp!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển Đổi Năm Dương Lịch Sang Âm Lịch")

# Tạo nhãn và ô nhập liệu cho năm Dương lịch
label_nam = tk.Label(root, text="Nhập năm Dương lịch:")
label_nam.pack(pady=5)
entry_nam = tk.Entry(root)
entry_nam.pack(pady=5)

# Tạo nút chuyển đổi
button = tk.Button(root, text="Chuyển đổi", command=convert_to_am_lich)
button.pack(pady=10)

# Tạo nhãn để hiển thị hình ảnh con giáp
label_img = tk.Label(root)
label_img.pack(pady=10)

# Chạy chương trình Tkinter
root.mainloop()