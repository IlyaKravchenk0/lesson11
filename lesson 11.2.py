class SituationByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = SituationByNull(10, 100)
print(SituationByNull.divide_by_null(10, 0))
print(SituationByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))