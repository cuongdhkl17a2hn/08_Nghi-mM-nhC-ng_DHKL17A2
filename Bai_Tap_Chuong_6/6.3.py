import threading

# Hàm in các số chẵn
def in_chan():
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"Số chẵn: {i}")

# Hàm in các số lẻ
def in_le():
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"Số lẻ: {i}")

# Tạo hai luồng
luong_chan = threading.Thread(target=in_chan)
luong_le = threading.Thread(target=in_le)

# Khởi chạy các luồng
luong_chan.start()
luong_le.start()

# Đợi các luồng hoàn thành
luong_chan.join()
luong_le.join()