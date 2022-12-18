# class Laptop:
#     def config(self):
#         print("ASUS","i7","1TB")
# laptop1=Laptop()
# # print(id(laptop1))
# laptop2=Laptop()
# # print(id(laptop2))

# # Laptop.config()
# laptop1.config()
# laptop2.config()


# class Laptop:
#     def __init__(self,name,processor):
#         self.name=name
#         self.processor=processor
#     def printOutput(self):
#         print("My laptop name is:  ",self.name,"and th eprocessor is ",self.processor)
# laptop1=Laptop("ASUS","i7")
# laptop2=Laptop("HP","i9")
# laptop1.printOutput()
# laptop2.printOutput()


# class Person:
#     def __init__(self,name,rollnumber):
#         self.name=name
#         self.rollnumber=rollnumber
#     def outprint(self):
#         print(self.name,self.rollnumber)
# person1=Person("Shubham",55)
# person2=Person("Shivam",44)
# print(id(person2))
# print(id(person1))


# class Person:
#     def __init__(self):
#         self.name="Shubham"
#         self.age=18
#     def updateName(self,name):
#         self.name=name
#     def compareAge(self,other):
#         if(self.age==other.age):
#             return True
#         else:
#             return False
# person1=Person()
# person2=Person()
# person2.name="Atul"       # it is called instance variable 
# print(person1.name)
# print(person2.name)
# person2.compareAge(person1)
# if person1.age==person2.age:
#     print("They have same age")
# else:
#     print("They have different age")
# print(person1.name,person1.age)
# print(person2.name,person2.age)


class Car:
    wheels=4
    def __init__(self,brand,mil):
        self.brand=brand
        self.mil=mil
car1=Car("BMW",10)
car2=Car("TESLA",8)
Car.wheels=3
print(car1.brand,car1.mil,car1.wheels)
print(car2.brand,car2.mil,car2.wheels)
