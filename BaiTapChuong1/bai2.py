class TS:
    """Lớp đại diện cho một thí sinh."""
    
    def __init__(self, name="", toan=0.0, ly=0.0, hoa=0.0):
        self.name = name          # Họ tên thí sinh
        self.toan = toan          # Điểm môn Toán
        self.ly = ly              # Điểm môn Lý
        self.hoa = hoa            # Điểm môn Hóa

    def total_score(self):
        """Tính tổng điểm của thí sinh."""
        return self.toan + self.ly + self.hoa

    def display_info(self):
        """In thông tin của thí sinh."""
        print(f"Họ tên: {self.name}")
        print(f"Điểm Toán: {self.toan}, Điểm Lý: {self.ly}, Điểm Hóa: {self.hoa}")
        print(f"Tổng điểm: {self.total_score():.1f}")

# Chương trình chính
if __name__ == "__main__":
    list_ts = []  # Danh sách thí sinh
    n = int(input("Nhập số thí sinh: "))
    
    for i in range(n):
        print(f"\nNhập thông tin cho thí sinh thứ {i + 1}:")
        name = input("Nhập họ tên: ")
        toan = float(input("Nhập điểm Toán: "))
        ly = float(input("Nhập điểm Lý: "))
        hoa = float(input("Nhập điểm Hóa: "))
        # Tạo đối tượng TS và thêm vào danh sách
        thí_sinh = TS(name, toan, ly, hoa)
        list_ts.append(thí_sinh)

    # Điểm chuẩn
    diem_chuan = 20
    print("\nDanh sách thí sinh trúng tuyển (Điểm chuẩn: 20):")
    
    # Lọc thí sinh trúng tuyển và sắp xếp theo tổng điểm
    ds_trung_tuyen = [ts for ts in list_ts if ts.total_score() >= diem_chuan]
    ds_trung_tuyen.sort(key=lambda x: x.total_score(), reverse=True)

    # In danh sách thí sinh trúng tuyển
    if ds_trung_tuyen:
        for ts in ds_trung_tuyen:
            ts.display_info()
    else:
        print("Không có thí sinh nào trúng tuyển.")
