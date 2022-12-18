class student:
    pass

class A:
    def __init__(self):
        print("This is init of Method A")
    def method1(self):
        print("This is method 1")
class B(A):
    def method2(self):
        print("This is method2")
class C(B):
    def method3(self):
        print("This is method3")
objA=A()
objB=B()
objC=C()
objC.method1()
