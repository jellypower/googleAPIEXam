class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

n1=[1,2,3]
n2=[4,5,6]
a=MappingSubclass((1,2,3,4,5))
print(a.items_list)
a.update(n1,n2)
print(a.items_list)