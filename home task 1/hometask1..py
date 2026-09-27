# class Person:
#     def __init__(self, name,age,city):
#         self.name = name
#         self.age =age
#         self.city = city

#     def introduce(self):
#         print(f"Меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}.")


# person1 = Person("Umar", 999, "UZBEKISTAN")
# person1.introduce()



# class Dog:
#     def __init__(self, name,breed, age):
#         self.name =name
#         self.breed =breed
#         self.age =age

#     def bark(self):
#         print(f"{self.name}гавкает: Гав-гав!")


# mydog = Dog("REX","UNKNOW",3)


# mydog.bark()




# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def Show_price(self):
#         print(self.name,self.price)

# apple=Product("apple",99)
# orange=Product("orange",88)
# watermelon=Product("watermelon",77)
# pear=Product("pear",.81)


# apple.Show_price()
# orange.Show_price()
# watermelon.Show_price
# pear.Show_price()







# class Rectangle:

#     def __init__(self,width,height):
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width*(self.height ** 2)

#     def perimeter(self):
#         return 2 * self.width * self.height

#     def is_square(self):
#         return self.width==self.height

# num =Rectangle(6, 11)
# num2 = Rectangle(7, 7)
# print(f"Rectangle 1({num.width}{num.height}):")
# print(f"Area:{num.area()}")
# print(f"Perimetir:{num.perimeter()}")
# print(f"plowad:{num.is_square()}")

# print()
# print(f"Rectangle 2 ({num2.width}{num2.height}):")
# print(f"Area: {num2.area()}")
# print(f"Perimeter: {num2.perimeter()}")
# print(f"plowad: {num2.is_square()}")


        



# class Wallet :
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self,amout):
#         self.balance+=amout
#         return self.balance+amout

#     def widthraw(self,amout):
#         self.balance+=amout
#         if amout > self.balance:
#             return "Недостаточно средств"
#         else:
#             return self.balance-amout


# n = Wallet("Abduloh", 100)

# print(n.deposit(100))
# print(n.widthraw(99))













    

        