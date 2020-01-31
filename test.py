""" Test du comportement de sotckage"""

class A:
    """AAA"""
    _static = []
    _list_instance = [] # static

    def __init__(self, x):
        self.x = x
        self.add_self()
    
    def add_static(self, b):
        self._static.append(b)

    def add_self(self):
        A._list_instance.append(self)

    def __str__(self):
        return 'merci'

class B:
    def __init__(self, a, x):
        if not isinstance(a, A):
            raise ValueError('first parameter must be instance of x <class>')
        self.a = a
        self.x = x
        self.a.add_static(self)
        print("a.x = " + str(self.a.x))



a = A(2)

print(str(len(a._static)) + '\n')

b = B(a, 'hello')

print(str(len(a._static)) + '\n')

print(A._list_instance)
print(a)

for x in A._list_instance:
    print(str(x))