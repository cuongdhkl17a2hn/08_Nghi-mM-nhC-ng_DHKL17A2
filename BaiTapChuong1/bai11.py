import math

class Triangle:
    """Lớp đại diện cho tam giác."""
    
    def __init__(self, a, b, c):
        self.a = a  # Cạnh a
        self.b = b  # Cạnh b
        self.c = c  # Cạnh c

    def perimeter(self):
        """Tính chu vi tam giác."""
        return self.a + self.b + self.c

    def area(self):
        """Tính diện tích tam giác theo công thức Heron."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class RightTriangle(Triangle):
    """Lớp đại diện cho tam giác vuông, kế thừa từ lớp tam giác."""
    
    def __init__(self, a, b):
        # a và b là hai cạnh góc vuông
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)  # Tính cạnh huyền

    def area(self):
        """Tính diện tích tam giác vuông."""
        return (self.a * self.b) / 2


class IsoscelesTriangle(Triangle):
    """Lớp đại diện cho tam giác cân, kế thừa từ lớp tam giác."""
    
    def __init__(self, base, side):
        # base là đáy, side là hai cạnh bên
        super().__init__(base, side, side)

    def area(self):
        """Tính diện tích tam giác cân."""
        height = math.sqrt(self.side**2 - (self.base / 2)**2)  # Tính chiều cao
        return (self.base * height) / 2


class EquilateralTriangle(IsoscelesTriangle):
    """Lớp đại diện cho tam giác đều, kế thừa từ lớp tam giác cân."""
    
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        """Tính diện tích tam giác đều."""
        return (math.sqrt(3) / 4) * self.a ** 2


# Chương trình chính
if __name__ == "__main__":
    # Nhập thông tin cho tam giác
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))
    triangle = Triangle(a, b, c)
    print(f"Chu vi tam giác: {triangle.perimeter()}")
    print(f"Diện tích tam giác: {triangle.area()}")

    # Nhập thông tin cho tam giác vuông
    a = float(input("Nhập cạnh góc vuông a của tam giác vuông: "))
    b = float(input("Nhập cạnh góc vuông b của tam giác vuông: "))
    right_triangle = RightTriangle(a, b)
    print(f"Chu vi tam giác vuông: {right_triangle.perimeter()}")
    print(f"Diện tích tam giác vuông: {right_triangle.area()}")

    # Nhập thông tin cho tam giác cân
    base = float(input("Nhập đáy của tam giác cân: "))
    side = float(input("Nhập cạnh bên của tam giác cân: "))
    isosceles_triangle = IsoscelesTriangle(base, side)
    print(f"Chu vi tam giác cân: {isosceles_triangle.perimeter()}")
    print(f"Diện tích tam giác cân: {isosceles_triangle.area()}")

    # Nhập thông tin cho tam giác đều
    side = float(input("Nhập cạnh của tam giác đều: "))
    equilateral_triangle = EquilateralTriangle(side)
    print(f"Chu vi tam giác đều: {equilateral_triangle.perimeter()}")
    print(f"Diện tích tam giác đều: {equilateral_triangle.area()}")
