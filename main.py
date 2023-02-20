class Factorial:
    def __init__(self):
        self.af = 0

    def __iter__(self):
        self.current = 1
        self.factorial = 1
        return self

    def __next__(self):
        self.factorial = self.factorial * self.current
        self.af = self.factorial - self.af
        self.current += 1
        return self.af


if __name__ == '__main__':
    q = iter(Factorial())
    print(type(q))
    for i in range(10):
        print(next(q))
