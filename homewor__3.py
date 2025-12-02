class MyList:
    def __init__(self,iterable = None):
        self._data = list(iterable) if iterable is not None else []

    def append(self,item):
        self._data.append(item)

    def pop(self, index = -1):
        return self._data.pop(index)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"MyList({self._data})"

lst = MyList([1, 2, 3])

lst.append(10)
print(lst)          

print(lst[0])       
print(len(lst))     

lst[1] = 999
print(lst)         

print(lst.pop())    
print(lst)         
