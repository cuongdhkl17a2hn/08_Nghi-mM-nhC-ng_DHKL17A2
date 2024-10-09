class NganXep:
    """Lớp ngăn xếp với dữ liệu là mảng float được cấp phát động."""
    
    def __init__(self, kich_thuoc):
        """Hàm tạo, khởi tạo ngăn xếp với kích thước cho trước."""
        self.kich_thuoc = kich_thuoc  # Kích thước tối đa của ngăn xếp
        self.ngan_xep = []              # Danh sách để lưu trữ các phần tử trong ngăn xếp

    def push(self, phan_tu):
        """Đưa một phần tử vào ngăn xếp."""
        if self.isFull():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.ngan_xep.append(phan_tu)
            print(f"Đã thêm {phan_tu} vào ngăn xếp.")

    def pop(self):
        """Lấy một phần tử ra từ đỉnh ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp trống! Không thể lấy phần tử.")
            return None
        return self.ngan_xep.pop()

    def isEmpty(self):
        """Kiểm tra ngăn xếp đã trống chưa."""
        return len(self.ngan_xep) == 0

    def isFull(self):
        """Kiểm tra ngăn xếp đã đầy chưa."""
        return len(self.ngan_xep) == self.kich_thuoc

    def count(self):
        """Trả về số lượng phần tử hiện tại trong ngăn xếp."""
        return len(self.ngan_xep)

    def print_stack(self):
        """In nội dung của ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp từ trên xuống dưới:")
            for phan_tu in reversed(self.ngan_xep):
                print(phan_tu)

    def __del__(self):
        """Hàm hủy, giải phóng tài nguyên (không cần thiết trong Python, nhưng có thể sử dụng để rõ ràng)."""
        print("Ngăn xếp đã bị hủy.")

# Chương trình chính để kiểm tra lớp NganXep
if __name__ == "__main__":
    kich_thuoc_ngan_xep = int(input("Nhập kích thước ngăn xếp: "))
    ngan_xep = NganXep(kich_thuoc_ngan_xep)

    # Thực hiện các thao tác với ngăn xếp
    while True:
        print("\n1. Đưa phần tử vào ngăn xếp (push)")
        print("2. Lấy phần tử ra khỏi ngăn xếp (pop)")
        print("3. Kiểm tra ngăn xếp trống")
        print("4. Kiểm tra ngăn xếp đầy")
        print("5. Đếm số phần tử trong ngăn xếp")
        print("6. In nội dung ngăn xếp")
        print("7. Thoát")
        lua_chon = input("Chọn thao tác (1-7): ")

        if lua_chon == '1':
            phan_tu = float(input("Nhập phần tử để đưa vào ngăn xếp: "))
            ngan_xep.push(phan_tu)
        elif lua_chon == '2':
            phan_tu_lay_ra = ngan_xep.pop()
            if phan_tu_lay_ra is not None:
                print(f"Đã lấy phần tử: {phan_tu_lay_ra}")
        elif lua_chon == '3':
            if ngan_xep.isEmpty():
                print("Ngăn xếp trống.")
            else:
                print("Ngăn xếp không trống.")
        elif lua_chon == '4':
            if ngan_xep.isFull():
                print("Ngăn xếp đã đầy.")
            else:
                print("Ngăn xếp không đầy.")
        elif lua_chon == '5':
            so_luong = ngan_xep.count()
            print(f"Số lượng phần tử trong ngăn xếp: {so_luong}")
        elif lua_chon == '6':
            ngan_xep.print_stack()  # Gọi phương thức để in nội dung ngăn xếp
        elif lua_chon == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
