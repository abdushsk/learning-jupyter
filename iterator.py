from functools import total_ordering

@total_ordering
class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def __eq__(self, other):
        return self.pay == other.pay

    def __lt__(self, other):
        return self.pay < other.pay

    def __repr__(self):
        return f"{self.name} : {self.pay}"
    
    
class FilterIter:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.count = -1
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count > (len(self.data) - 1):
            raise StopIteration
        val = self.key(self.data[self.count]) if self.key is not None else self.data[self.count]
        if val % 2 == 0:
            return self.__next__()
        return self.data[self.count]

class SmartArray(list):
    def __init__(self, item=None, key=None):
        self.key = key
        if item == None:
            super().__init__()
        else:
            super().__init__(item)
    
    def __iter__(self):
        return FilterIter(self, self.key)

# z = SmartArray([1,2,3,4]) 

# for k in z:
#     print(k)
e1 = Employee("Raj",1)
e2 = Employee("Isho",2)
e3 = Employee("Abdush",1)
e4 = Employee("Gang",3)

print(e1 >= e2)
print(e1 < e2)
print(e1 <= e3)


arr = SmartArray(key=lambda x: x.pay)
arr.extend([e1,e2,e3,e4])
for z in arr:
    print(z)
    
arr2 = SmartArray()
arr2.extend([1,2,1,3])


for z in arr2:
    print(z)