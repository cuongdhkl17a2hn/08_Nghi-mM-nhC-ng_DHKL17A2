class DaGiac:
    """Lớp đại diện cho đa giác."""
    
    def __init__(self, so_canh):
        self.so_canh = so_canh  # Số cạnh của đa giác


class HinhBinhHanh(DaGiac):
    """Lớp đại diện cho hình bình hành, kế thừa từ lớp đa giác."""
    
    def __init__(self, canh_dai, canh_ngan):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.canh_dai = canh_dai  # Cạnh dài
        self.canh_ngan = canh_ngan  # Cạnh ngắn

    def chu_vi(self):
        """Tính chu vi hình bình hành."""
        return 2 * (self.canh_dai + self.canh_ngan)

    def dien_tich(self, chieu_cao):
        """Tính diện tích hình bình hành."""
        return self.canh_dai * chieu_cao


class HinhChuNhat(HinhBinhHanh):
    """Lớp đại diện cho hình chữ nhật, kế thừa từ lớp hình bình hành."""
    
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)  # Hình chữ nhật có chiều dài và chiều rộng

    def dien_tich(self):
        """Tính diện tích hình chữ nhật."""
        return self.canh_dai * self.canh_ngan


class HinhVuong(HinhChuNhat):
    """Lớp đại diện cho hình vuông, kế thừa từ lớp hình chữ nhật."""
    
    def __init__(self, canh):
        super().__init__(canh, canh)  # Hình vuông có cạnh bằng nhau

# Chương trình chính
if __name__ == "__main__":
    # Nhập thông tin cho hình bình hành
    canh_dai = float(input("Nhập cạnh dài của hình bình hành: "))
    canh_ngan = float(input("Nhập cạnh ngắn của hình bình hành: "))
    chieu_cao = float(input("Nhập chiều cao của hình bình hành: "))
    
    hinh_binh_hanh = HinhBinhHanh(canh_dai, canh_ngan)
    print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
    print(f"Diện tích hình bình hành: {hinh_binh_hanh.dien_tich(chieu_cao)}")

    # Nhập thông tin cho hình chữ nhật
    chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    
    hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
    print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
    print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.dien_tich()}")

    # Nhập thông tin cho hình vuông
    canh = float(input("Nhập cạnh của hình vuông: "))
    
    hinh_vuong = HinhVuong(canh)
    print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
    print(f"Diện tích hình vuông: {hinh_vuong.dien_tich()}")
