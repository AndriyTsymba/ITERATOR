# теорія
#1 ітератори
lst= [1,2,3,4,5,6,6]
print(iter(lst))

class MyIterator:
    def __init__(self,date):
        self.date = date
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.date):
            raise MyIterator
        value =self.date[self.index]
        self.index += 1
        return value
for num in MyIterator(lst):
     print(num)
#2
def my_generator(data):
    for item in data:
        yield item

for num in my_generator(lst):
    print(lst)
#3 калькулятор
def Calculatore():
    def add(a,b):
       return a+b
    def sub(a,b):
        return a-b
    def mult(a,b):
        return a*b
    def div(a,b):
        if b != 0:
            return a/b
        else:
            raise ValueError("Divizion by zero")
    return add,sub,mult,div
# створення замикання
aad,sub,mult,div = calc()
print(div(3,0))


