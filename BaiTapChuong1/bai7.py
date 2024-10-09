class Date:
    """Lớp đại diện cho một ngày, tháng, năm."""
    
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin về ngày ra màn hình."""
        print(f"Ngày: {self.day:02}/{self.month:02}/{self.year}")

    def is_leap_year(self, year):
        """Kiểm tra năm nhuận."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def days_in_month(self, month, year):
        """Tính số ngày trong tháng."""
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        return 0

    def next(self):
        """Tính ngày tiếp theo."""
        self.day += 1
        if self.day > self.days_in_month(self.month, self.year):
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

# Chương trình chính
if __name__ == "__main__":
    # Nhập thông tin ngày
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    
    date = Date(day, month, year)
    
    # Hiển thị thông tin ngày
    date.display()
    
    # Tính và hiển thị ngày tiếp theo
    date.next()
    print("Ngày tiếp theo:")
    date.display()
