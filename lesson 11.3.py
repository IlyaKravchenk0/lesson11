class Erroooor:
    def __init__(self, *args):
        self.my_test = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_test.append(val)
                print(f'Текущий список - {self.my_test} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_n = input(f'Попробовать еще раз? Y/N ')

                if y_n == 'Y' or y_n == 'y':
                    print(try_except.my_input())
                elif y_n == 'N' or y_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Erroooor(1)
print(try_except.my_input())