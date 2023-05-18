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
