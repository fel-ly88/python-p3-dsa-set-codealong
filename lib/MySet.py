class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
            
    def has(self, value):
     return value in self.dictionary
     
    def add(self, value):
     self.dictionary[value] = True
     return self
 
    def delete(self, value):
     self.dictionary.pop(value, None)
     return self
 
    def size(self):
     return len(self.dictionary)
 
    def clear(self):
        self.dictionary.clear()
        return self

    def __str__(self):
        set_list = [str(k) for k in self.dictionary]
        return f'MySet: {{{", ".join(set_list)}}}'

s = MySet([1,2,3,3])
print(s)       
s.add(4)
print(s)       
s.delete(2)
print(s.has(2))
print(s.size()) 
s.clear()
print(s)      
