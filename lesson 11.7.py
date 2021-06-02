class CompleteNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.y = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма y1 и y2 равна')
        return f'y = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение y1 и y2 равно')
        return f'y = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'y = {self.a} + {self.b} * i'


z_1 = CompleteNumber(1, -2)
z_2 = CompleteNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)