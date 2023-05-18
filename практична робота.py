class OddIterator:
    def __init__(self, N):
        if N <= 0:
            raise ValueError
        self.N = N
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        if self.current % 2 != 0:
            number = self.current
            self.current += 2
            return number
        else:
            self.current += 1
        return self.__next__()
try:
    iterator = OddIterator(10)
    for number in iterator:
        print(number)
except ValueError as e:
        print(str(e))
except StopIteration:
        print("Кінець")



