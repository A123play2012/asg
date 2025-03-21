class asg(type):
    def __init__(self, *args):
        def __init__(self, *object):
            if self and object:
                self.__object = str(str(object[0]))
            else:
                self.__object = ''
        
        def __repr__(self):
            try:
                return str(self.object1[0]) + self.__object + str(self.object1[1])
            except:
                return self.object2[0] + self.__object + self.object2[1]
        
        def __str__(self):
            return self.__object
        
        def __add__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, self):
                return self(obj1.__object + obj2.__object)
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __mul__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, int):
                return self(str(obj1.__object) * int(obj2))
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __eq__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, self):
                if obj1.__object == obj2.__object:
                    return True
                else:
                    return False
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __ge__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, self):
                if obj1.__object >= obj2.__object:
                    return True
                else:
                    return False
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __le__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, self):
                if obj1.__object <= obj2.__object:
                    return True
                else:
                    return False
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __gt__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, self):
                if obj1.__object > obj2.__object:
                    return True
                else:
                    return False
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __lt__(obj1, obj2):
            if isinstance(obj1, self) and isinstance(obj2, self):
                if obj1.__object < obj2.__object:
                    return True
                else:
                    return False
            else:
                raise TypeError(f'Can only concatenate {type(obj1)} (not "{type(obj2)}") to {type(obj1)}')
        
        def __len__(obj1):
            if isinstance(obj1, self):
                return len(str(self.__object))
            else:
                pass
        
        object2 = '||'
        
        self.__init__ = __init__
        self.__repr__ = __repr__
        self.__str__ = __str__
        self.__add__ = __add__
        self.__mul__ = __mul__
        self.__eq__ = __eq__
        self.__ge__ = __ge__
        self.__gt__ = __gt__
        self.__le__ = __le__
        self.__lt__ = __lt__
        #self.__len__ = __len__
        self.object2 = object2
