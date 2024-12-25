import threading

# Hàm viết các số chẵn
def viet_chan(nguong):
    for i in range(2, nguong + 1, 2):
        print(f"Số chẵn: {i}")

# Hàm viết các số lẻ
def viet_le(nguong):
    for i in range(1, nguong + 1, 2):
        print(f"Số lẻ: {i}")

# Ngưỡng số cần đạt
nguong = 20

# Tạo hai luồng
luong_chan = threading.Thread(target=viet_chan, args=(nguong,))
luong_le = threading.Thread(target=viet_le, args=(nguong,))

# Khởi chạy các luồng
luong_chan.start()
luong_le.start()

# Đợi các luồng hoàn thành
luong_chan.join()
luong_le.join()