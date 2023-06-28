'''Class D inherits from class C, 
which in turn inherits from classes A and B. 
Class D accesses the immediate superclass of class D, 
which is class C and resolves the value of the variable once it's found in that superclass.
'''
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    def b(self):
        return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b())