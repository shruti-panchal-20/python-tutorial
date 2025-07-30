#
#print (34!=34)



#print(7 < 100 and 34==34)


#print (126>130)

#print((456==456)!=(235==236))

# jutuyil;open

# ikujghf



# lkjhgbfd



# ytvnhb
# DeprecationWarningw

# returner
# return
# raiseer
# raiseer
# raiseer
# raisee
# r

# ----17 july





# a = int(input("Tell your number"))

# while a > 0:
#     print (a % 10)
#     a= a//10

    



# a = int(input("Tell your number"))


# rev = 0

# while a > 0:
        
#         rev = rev *10+ a% 10

#         a=a//10
# print(rev) 


# def hello():
#   print("hello this is a function by me")


# hello()   


# def sum(a,b):
#   print(f"The sum of both numbers is {a+b}")

# sum(3,4)

# sum (5,6)


# def hello(name,age):
#    print(f"Your name is {name} and age is {age}")

# hello("Shruti","17")

#  sum(a,b=20def):
#   print(f"The sum of numbers is {a+b}")

# sum(22)  

# sum(22,22)

# def palindrome(st):
#   rev = ""

#   for i in range(len(st)-1,-1,-1):
#     rev= rev + st[i]

#   if rev == st:
#     print(f"{st}  is a palindrome")

#   else:
#     print(f"{st}is not a palindrome")

# palindrome("NAMAN")
# palindrome("SHRUTI")

# a = [1,2,3,4,5.6]

# for i in range(len(a)):
#     print(a[i])


# 


# help(list)


# l = [2,3,4,5,6]

# l.insert(2,56)
# print (l)


# l = [3,-9,8,-6,-5,7,2]

# print("positive elements are")
# for i in l:
#   if i >= 0:
#     print(i)

# print("negative elements are")
# for i in l:
#   if i < 0:
#     print(i)

# l = [34,56,78,45,99,455,99]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#   if l[i] > largest:
#     largest=l[i]
#     index=i
# print (f"your largest number is {largest} at index{index}")    

# l = [13,12,14,15,16,17]

# largest=l[0]
# first_index=0
# sec_largest=l[0]
# sec_largest=0

# for i in range(len(l)):
#   if l[i] > largest:
#     sec_largest=largest
#     largest=l[i]
#   elif i>sec_largest:
#     sec_largest=i   

# print(f"largest number is {largest} with index {first_index} and second largest is {sec_largest} with index{sec_largest}")    


# a=[12,13,14,15]

# for i in range(len(a)-1):
#   if a [i]< a[i+1]:
#     continue 
#   else:
#     print("your list is not sorted")
#     break

# else:
#   print("your list is sorted") 



#20/07/25


#TUPLE:-

# a=(1,2,3,4)

# print(type(a))

# a = (1,2,3,4,5,5,5,5,5,5,5,5,5,5,5.5,print(),"hello")

# count = a.count(5)

# print(count)



# index = a.index(5)
# print(index)

# #SETS:-

# a = {1,2,3,4,"hello",7,5,9,6}

# for i in a:
#  print(i)

# a = [1,2,3,4]
# a[3]=400
# print(a)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8,9}

# s = a^b

# print(s)



# 22/07/25------  *DICTIONARIES*

# a = {}           #In this way dictionaries are created .
# print (type(a))


# d = {10:100,20:200,30:300}

# print(d[10])  
# d[10]= 67   #updating
# d[50]=569   #creating
# del d[30]   #deleting
# print(d)


# #help(dict)

# d = {1:10,2:20,3:30,4:40}

# for i in d:
#  print (i) 

# f = d.get(20)
# print(d.items())


# d = {1:10,2:20,3:30,4:40}
# sum = 0

# for i in d:
#   sum = sum + d[i]

# print(sum)


# 1 : 3
# 2 : 4
# 3 : 2

# a = [x,x,x,y,y,y,y,z,z]

# a = [1,1,1,2,2,2,2,3,3]

# d = {}
# for i in a:
#   if i in d.keys():
#     d[i] +=1  
#   else:
#     d[i] = 1

#     print(d) 



#22/07/25

# a = int(input("tell your number"))

# try:
#     print(10/a)

# except ZeroDivisionError:
#     print("sorry you cannot divide by 0")

# print("ok i have done the division")          


# a = int(input("tell your number"))

# try:
#     print(10/a)

# except Exception as err:
#      print(f"sorry there is an err as {err}")

# else:
#      print("good there is no exception")

# print("ok i have done the division")


# 26/07/25   object oriented progaramme .

# class Factory:
#   a = 12 #  attribute 

#   def hello(self): # method 
#     print("how are you")

#   print('hello i am getting initialised')


# obj= Factory()

# print(obj.a)


# print(Factory().a)

# Factory().hello()


# class Factory:
#   def __init__(self,material,zips,pockets): 
#     print(self)

#     self.material=material
#     self.zips=zips
#     self.pockets=pockets

#   def show(self):
#     print(f"your object details are {self.material},{self.zips},{self.pockets}") 



# reebok = Factory("leather",3,2)
# campus = Factory("nylon",4,1)

# # print(campus.pockets)
# # print(reebok.material)

# reebok.show()



# class Animal:
#   name = "lion" #class attribute

#   def __init__(self,age):
#    self.age = age #instance attribute

#   def show(self): #instance method 
#     print(f"how are you your age is {self.age}")

#   @classmethod
#   def hello(cls):
#     print("how are you brother") 

#   @staticmethod
#   def static():
#     print("how are you")


# obj = Animal(12)

# obj.show()

# class FactoryAnand: # parent class / super class 
#   a = " I am an attribute mentioned inside a Factory"
#   def hello(self):
#     print("hello i am a method inside a Factory")

# class Factorypune(FactoryAnand):   
#   pass

# obj = FactoryAnand()

# obj2 = Factorypune()


# print(obj2.hello())

# class Animal:
#   def __init__(self,name):
#     self.name = name       

#   def show(self):
#     print(f"hello your name is {self.name}")


# class Human(Animal):      
#     pass
  

# animal1 = Animal("lion")
# person1 = Human("Shruti")


# # person1.show()
# animal1.show()


# class Animal:
#   def __init__(self,name):
#     self.name = name

#   def show(self):
#     print(f"hello your name is {self.name}")


# class Human(Animal):
#   def __init__(self, name,age):
#     super().__init__(name)   
#     self.age = age

#   def show(self):
#     print(f"hello your name is {self.name},{self.age}")    


# animal1 = Animal("lion")
# person1 = Human("shruti,17")

# person1.show()




#30/07/25 

class Animal:
  def show(self):
    print("Hello I am Shruti")


class Human (Animal):
  def show(self):
    print("how are youuuu")    


obj =Human()
obj.show()



class Animal:
  def show(self):
    print("I am running")


class Human:
  def show (self):
    print("Hello, I am also running")    


obj = Animal()
obj2 = Human()


obj.show()
obj2.show()




class Factory:
  _a = "pune"

  def show(self):
    print("hello, I am a pune factory")

class Bhopal(Factory):
  def show2 (self):
    print(super()._a)

obj = Bhopal()
obj.show2() 