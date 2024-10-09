class Date:
    """Lớp đại diện cho một ngày, tháng, năm."""
    
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin ngày."""
        return f"{self.day:02}/{self.month:02}/{self.year}"

class Employee:
    """Lớp đại diện cho một nhân viên."""
    
    def __init__(self, name, birth_date, join_date):
        self.name = name              # Họ tên nhân viên
        self.birth_date = birth_date  # Ngày sinh
        self.join_date = join_date    # Ngày vào công ty

    def display_info(self):
        """In thông tin của nhân viên."""
        print(f"Họ tên: {self.name}")
        print(f"Ngày sinh: {self.birth_date.display()}")
        print(f"Ngày vào công ty: {self.join_date.display()}")

# Chương trình chính
if __name__ == "__main__":
    # Nhập thông tin nhân viên
    name = input("Nhập họ tên nhân viên: ")
    
    day_of_birth = int(input("Nhập ngày sinh: "))
    month_of_birth = int(input("Nhập tháng sinh: "))
    year_of_birth = int(input("Nhập năm sinh: "))
    birth_date = Date(day_of_birth, month_of_birth, year_of_birth)

    day_of_join = int(input("Nhập ngày vào công ty: "))
    month_of_join = int(input("Nhập tháng vào công ty: "))
    year_of_join = int(input("Nhập năm vào công ty: "))
    join_date = Date(day_of_join, month_of_join, year_of_join)

    # Tạo đối tượng nhân viên
    employee = Employee(name, birth_date, join_date)
    
    # Hiển thị thông tin nhân viên
    employee.display_info()
