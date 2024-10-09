import math

class Diem:
    """Lớp đại diện cho một điểm trong không gian 2D."""
    
    def __init__(self, x=0, y=0):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y


class Elip(Diem):
    """Lớp đại diện cho elip, kế thừa từ lớp điểm."""
    
    def __init__(self, x, y, a, b):
        super().__init__(x, y)  # Gọi hàm khởi tạo của lớp cha
        self.a = a  # Bán trục lớn
        self.b = b  # Bán trục nhỏ

    def dien_tich(self):
        """Tính diện tích elip."""
        return math.pi * self.a * self.b


class DuongTron(Elip):
    """Lớp đại diện cho đường tròn, kế thừa từ lớp elip."""
    
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)  # Đường tròn là elip với bán trục lớn = bán trục nhỏ
        self.r = r  # Bán kính

    def dien_tich(self):
        """Tính diện tích đường tròn."""
        return math.pi * self.r ** 2


# Chương trình chính
if __name__ == "__main__":
    # Nhập thông tin cho elip
    x = float(input("Nhập tọa độ x của elip: "))
    y = float(input("Nhập tọa độ y của elip: "))
    a = float(input("Nhập bán trục lớn (a) của elip: "))
    b = float(input("Nhập bán trục nhỏ (b) của elip: "))
    
    elip = Elip(x, y, a, b)
    print(f"Diện tích elip: {elip.dien_tich()}")

    # Nhập thông tin cho đường tròn
    x = float(input("Nhập tọa độ x của đường tròn: "))
    y = float(input("Nhập tọa độ y của đường tròn: "))
    r = float(input("Nhập bán kính (r) của đường tròn: "))
    
    duong_tron = DuongTron(x, y, r)
    print(f"Diện tích đường tròn: {duong_tron.dien_tich()}")
