import math

class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        """Kiểm tra phân số hợp lệ (mẫu số phải khác 0)"""
        return self.mau_so != 0

    def nhap_phan_so(self):
        """Nhập tử số và mẫu số từ người dùng và kiểm tra tính hợp lệ"""
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while self.mau_so == 0:
            print("Mẫu số phải khác 0, vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def in_phan_so(self):
        """In phân số dưới dạng a/b"""
        if self.mau_so == 1:
            print(f"Phân số: {self.tu_so}")
        else:
            print(f"Phân số: {self.tu_so}/{self.mau_so}")

    def rut_gon(self):
        """Rút gọn phân số về dạng tối giản"""
        ucln = math.gcd(self.tu_so, self.mau_so)  
        self.tu_so //= ucln
        self.mau_so //= ucln

        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so

if __name__ == "__main__":
    ps = PhanSo()
    ps.nhap_phan_so()

    print("\nPhân số ban đầu:")
    ps.in_phan_so()

    ps.rut_gon()
    print("\nPhân số sau khi rút gọn:")
    ps.in_phan_so()
