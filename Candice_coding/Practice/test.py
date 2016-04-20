class A(object):
    def __init__(self):
        self.a = 0
        A.b = 1

a1 = A()
print a1.a, a1.b
A.b = 2
a2 = A()
print a1.a, a1.b, A.b
print a2.a, a2.b, A.b