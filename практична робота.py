#2
class SquareGenerator:
    def __init__(self, N):
        if not isinstance(N, int):
            raise TypeError
        self.N = N
    def generate_squares(self):
        for i in range(self.N +1 ):
            yield i ** 2
try:
    n = int(input("Введіть число "))
    generator = SquareGenerator(n)
    squares = generator.generate_squares()
    for i in squares:
        print(i)
except TypeError as e:
    print(e)
except ValueError:
    print("Введіть коректне  число.")





