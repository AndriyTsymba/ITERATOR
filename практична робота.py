#3
lst= [1,2,3,4,5,6,6]
print(iter(lst))
class ListIterator:
    def __init__(self,date):
        self.date = date
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.date):
            raise ListIterator
        value =self.date[self.index]
        self.index += 1
        return value
for num in ListIterator(lst):
     print(num)




