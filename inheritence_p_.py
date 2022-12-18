# a="hello World"
# b=[1,2,3,4,5,6]
# print(len(b))
# print(len(a))



# def add(a,b,c=5):
#     return a+b+c
# print(add(1,2))
# print(add(1,2,3))




class Rect:
    def calculateArea(self,length=None,bredth=None):
        if length!=None and bredth!=None:
            return length*bredth
        elif length!=None:
            return length*length
Rectangle=Rect()
print(Rectangle.calculateArea(2,3))
print(Rectangle.calculateArea(2))




