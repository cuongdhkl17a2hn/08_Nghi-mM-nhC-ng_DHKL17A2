import threading

# Hàm để in tên của mỗi luồng
def in_ten_luong():
    print(f"Đây là luồng: {threading.current_thread().name}")

# Tạo nhiều luồng
luong_1 = threading.Thread(target=in_ten_luong, name="Luồng 1")
luong_2 = threading.Thread(target=in_ten_luong, name="Luồng 2")
luong_3 = threading.Thread(target=in_ten_luong, name="Luồng 3")

# Khởi chạy các luồng
luong_1.start()
luong_2.start()
luong_3.start()

# Đợi các luồng hoàn thành
luong_1.join()
luong_2.join()
luong_3.join()