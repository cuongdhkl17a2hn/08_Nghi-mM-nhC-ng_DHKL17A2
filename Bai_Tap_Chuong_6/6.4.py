import threading

# Hàm tính giai thừa
def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"Giai thừa của {n} là: {result}")

# Tạo các luồng tính giai thừa
luong_1 = threading.Thread(target=tinh_giai_thua, args=(5,))
luong_2 = threading.Thread(target=tinh_giai_thua, args=(7,))

# Khởi chạy các luồng
luong_1.start()
luong_2.start()

# Đợi các luồng hoàn thành
luong_1.join()
luong_2.join()