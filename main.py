class Factorial:
    def __init__(self):  # инициализируем класс
        self.af = 0  # задаем начальное значение суммы

    def __iter__(self):  # тут мы создаем итератор
        self.current, self.factorial = 1, 1  # задаем начальные значения текущего номера элемента
        # и значение его факториала соответственно
        return self  # возвращаем итератор

    def __next__(self):  # метод класса осуществляющий вычисление каждого последующего значения суммы
        self.factorial = self.factorial * self.current  # вычисляем значение факториала
        self.af = self.factorial - self.af  # вычисляем значение суммы
        self.current += 1  # прибавляем единичку к счетчику
        return self.af  # возвращаем значение суммы


if __name__ == '__main__':
    q = iter(Factorial())  # создаем итератор класса
    print(type(q))  # проверяем тип элемента
    for i in range(10):  # перебираем первые 10 итераций "ГЕНЕРАТОРА"
        print(next(q))  # выводим значения по порядку
