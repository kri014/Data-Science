# oops concept

class Student:
	def __init__(self): # initilizing the variable
		print("the constructor execution")
		self.name="durga"
		self.rollno=1010
		self.marks=90
	def talk(self):
		print("hello i am :",self.name)
		print("my roll no:",self.rollno)
		print("my marks is :",self.marks)

s = Student()# creating a Student class
print(s.name)
print(s.rollno)
print(s.marks)
---------------------
# Calss with the dynamic input 
class Student:
	def __init__(self,name,rollno,marks): # initilizing the variable
		print("the constructor execution")
		self.name=name
		self.rollno=rollno
		self.marks=marks
	def talk(self):
		print("hello i am :",self.name)
		print("my roll no:",self.rollno)
		print("my marks is :",self.marks)
s1 = Student("sunny",101,90)
print("Student 1 Details:",s1.name,s1.rollno,s1.marks)
s2=  Student("Bunny",102,95)
print("Student 2 Details:",s2.name,s2.rollno,s2.marks)


-----------------------------
# post mortom of the self:
	
# both self and the having the same address

class Test:
	def __init__(self):
		pass
t = Test()
--------
# both self and the having the same address

class Test:
	def __init__(self):
		print("The address of the object reffered by self:",id(self))
	
t = Test()
print("The address of the object reffered by t :",id(t))
----------------

class Test:
	def __init__(self):
		print("Constructor")
	def m1(self,x):
		print("method")
	
t = Test()
t.m1(34)# we have to give the value of x
------------------------------------------
# self is not the keyword here we are using the telf insted of the self

class Student:
	def __init__(telf,name,rollno,marks): # initilizing the variable
		print("the constructor execution")
		telf.name=name
		telf.rollno=rollno
		telf.marks=marks
	def talk(telf):
		print("hello i am :",telf.name)
		print("my roll no:",telf.rollno)
		print("my marks is :",telf.marks)
s1 = Student("sunny",101,90)
print("Student 1 Details:",s1.name,s1.rollno,s1.marks)
s2=  Student("Bunny",102,95)
print("Student 2 Details:",s2.name,s2.rollno,s2.marks)
----------------------------------
class Student:
	def __init__(telf,name,rollno,marks): # initilizing the variable
		print("the constructor execution")
		telf.name=name
		telf.rollno=rollno
		telf.marks=marks
	def talk(x): # we can provide the method variable 
		print("hello i am :",x.name)
		print("my roll no:",x.rollno)
		print("my marks is :",x.marks)
s1 = Student("sunny",101,90)
print("Student 1 Details:",s1.name,s1.rollno,s1.marks)
s2=  Student("Bunny",102,95)
print("Student 2 Details:",s2.name,s2.rollno,s2.marks)

--------------------------------------
# here we can give any variable in with respect to self
class Test:
	def __init__(x):
		print("Constructor")
	
t = Test()
-----------------
class Test:
	def __init__(x):
		print("Constructor")
	
t = Test(10) # if we give value here it will show error as pvm already assign the value to x
             # even then we are giving the value to the to the x in Test(10)
			 #TypeError: __init__() takes 1 positional argument but 2 were given

----------------------------------------------
class Test:
	def __init__():# there is nothing is varialbe is assign so it will show error
		print("Constructor")
	
t = Test() # but here PVM will assign the value
           #    t = Test() # but here PVM will assign the value
           #    TypeError: __init__() takes 0 positional arguments but 1 was given
-------------------------------------------
class Employee:
	def __init__(self,name,age,salary):
		self.name = name 
		self.age = age
		self. salary= salary
	def bonous(self):
		print("The emplpyee :",self.name)
		print("age:",self.age)
		b= self.salary*0.1
		return b

c = Employee("Sunny",26,100000)
print(c.bonous())
-------------------
class Test:
	def __init__(self,name):
		self.name=name
	
t = Test("Durga") # initial name is Durga 
print(t.name)
t.__init__("Sunny")# the sunny name is changed at this point
print(t.name)
-------------------------------------
# with two different class
class Test:
	def __init__(self,name):
		self.name=name
	
class Demo:
	def __init__(self,name):
		self.name=name

t = Test("sunny")
print(t.name)
d= Demo("Bunny")
print(d.name)
----------------------
# with two different class
class Test:
	def Test(self):
		print("a special method")

t= Test()# __init__ will be executed so nothing will return
t.Test()# now we call the method so "a special method will execute

-------------------
# the combination of both function and class 
# the execution will be held only for the recent one 
def Test():
	print("Test Function")

class Test:
	def Test(self):
		print("Method Test")

t = Test()
------------------------------
# wac to get the movie datails 
class Movie:
	def __init__(self,title,hero,heroine):
		self.title= title
		self.hero= hero
		self.heroine=heroine

	def info(self):
		print("Title name:",self.title)
		print("Hero name:",self.hero)
		print("Heroine name:",self.heroine)

	
l =[]
while True:
	movie= input("Enter Movie name :")
	hero= input("Enter Hero name :")
	heroine= input("Enter heroine name:")
	m = Movie(movie,hero,heroine)
	l.append(m)
	option = input("Do you want to add more details:[yes|no]")
	if option.lower()=="no":
		break
print("All movie details ")
print("#"*50)
for movie in l:
	movie.info()
	print()

----------------------------
# Types  of varible
#1. Instance variable
#2. Static variable
#3. Local  Variable  
class Student:
	collegeName="Durgasoft" # Static Variable
	def __init__(self,name,rollno):
		self.name =  name # name and rollno with self is instance varible
		self.rollno = rollno

	def m1(self):
		x=10 # local  varibale (in method)
		for i in range(x):
			print(i)

---------------------------
# Types  of  Method
#1. Instance method
#2. Class  Method 
#3. Static Method

class Student:
	collegeName="Durgasoft" # Static Variable
	def __init__(self,name,rollno):
		self.name =  name # name and rollno with self is instance varible
        self.rollno = rollno
	def getstudent_info(self):# 
		print("The student name :",self.name)
		print("The rollno:",self.rollno)
	def getcollege_info():# this method  uses only static varible so  it is called as syatic method
		print("college name is :",collegeName) 

	def m1(self):
		x=10 # local  varibale (in method)
		for i in range(x):
			print(i)
----------------------------
class Student:
	collegeName="Durgasoft"
	director='Nagoor'
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	def getstudent_info(self):
		print("The student name :",self.name)
		print("The rollno:",self.rollno)
	@ classmethod #class decorator
	def getcollege_info(cls): # class level object referenc
		print("College name is :",cls.collegeName)
		print("Director name is :",cls.collegeName)

	@ staticmethod # static method holds local variable
	def get_average(a,b,c):
		return (a+b+c)/3

s= Student("Durga",101)
s.getstudent_info()
s.getcollege_info()
average=s.get_average(10,20,30)
print(average)
-----------------
class Test:
	def __init__(self):
		self.a=20 # instance varible inside the constructor
		self.b=20

	def m1(self):
		self.c=30 # instance varible in the method

t = Test()
t.m1()
t.d=40
t.e=50 # instance varible at the outside the class
print(t.__dict__)
------------------------------
# Acessing the instance varible
class Test:
	def __init__(self):
		self.a=10
		self.b=20

	def m1(self):
		print(self.a)# acessing the instance varible in the inside the class
		print(self.b)

t = Test()
t.m1()
print(t.a)# ascessing the instance varible outside the class
print(t.b)
--------------------------------------
# Deleting the variable
class Test:
	def __init__(self):
		self.a=10
		self.b=20
		self.c=30
		self.d=40

	def m1(self):
		del self.a # deleting inside the class
		
t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.b # deleting outside the class
print(t.__dict__)
-------------------------------
# updating the variable
class Test:
	def __init__(self):
		self.a=10
		self.b=20
		self.c=30
		self.d=40

	def m1(self):
		del self.a # deleting inside the class
		
t1 = Test()
t1.a=777
t1.b=888
print(t1.__dict__)
t2=Test() 
print(t2.__dict__)
--------------------------
# Deleting the variable
class Test:
	def __init__(self):
		self.a=10
		self.b=20
		self.c=30
		self.d=40

	def m1(self):
		del self.a # deleting inside the class
		
t1 = Test()
t1.m1() # deleting in object t1
print(t1.__dict__)
t2=Test() 
print(t2.__dict__)

---------------------------------
# Setter and getter
# 1. if we know the data at the time of the crating the object:construtor
#2. if we don't know data at the time of creating an object: 
#            create object and later by using setter method we can perform initilization

class Student:
	def setName(self,name):
		self.name=name
		
	def getName(self):
		return self.name

	def setMarks(self,marks):
		self.marks=marks
		
	def getMarks(self):
		return self.marks

n= int(input("Enter the number of students :"))
for i in range(n):
	s=Student()
	name = input("Enter the Name: ")
	s.setName(name)
	marks=int(input("Enter the marks :"))
	s.setMarks(marks)
	print("Hi", s.getName())# dont put name again here
	print("your marks are ",s.getMarks())# dont put marks again in the get statement
	print()

--------------
# Setter and getter
# 1. if we know the data at the time of the crating the object:construtor
#2. if we don't know data at the time of creating an object: 
#            create object and later by using setter method we can perform initilization

class Student:
	def setName(self,name):
		# validation
		self.name=name
		
	def getName(self):
		#validation
		return self.name

	def setMarks(self,marks):
		self.marks=marks
		
	def getMarks(self):
		return self.marks

s=Student()
name = input("Enter the Name: ")
s.setName(name)
marks=int(input("Enter the marks :"))
s.setMarks(marks)
print("Hi", s.getName())# dont put name again here
print("your marks are ",s.getMarks())# dont put marks again in the get statement
print()

---------------------
class Animal:
	legs=4
	@classmethod
	def walk(cls,name):
		print("{} walks through {} legs".format(name,cls.legs))

Animal.walk("cat")
-------------------------
class Student:
	collegeName="Durgasoft"
	@classmethod
	def getcollegeinfo(cls):
		print("College Name",cls.collegeName)

Student.getcollegeinfo()
------------------------------------------------
# static method
class Durgamath:

	@staticmethod
	def add(x,y):
		print("The sum:",x+y)

	@staticmethod
	def product(x,y):
		print("The sum:",x*y)
		
	@staticmethod
	def average(x,y):
		print("The sum:",(x+y)/2)

Durgamath.add(10,20)
Durgamath.product(10,20)
d=Durgamath()
d.average(10,20)
---------------------------------
class  Employee:
	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal
	def display(self):
		print('Employee Number',self.eno)
		print('employee Name',self.ename)
		print('Employee Salary',self.esal)

class  Manager:
	'''Here we are not using any instance method
	   it is a static method'''
	def updateSalary(emp):
		emp.esal=emp.esal+10000
		emp.display()

e=Employee(872567,"Durga",70000)
Manager.updateSalary(e)
--------------------------------------------
# nested class
class Outer:
	def __init__(self):
		print("Outer class object Creation")
	class Inner:
		def __init__(self):
			print("Inner calss object Creation")

		def m1(self):
			print("Inner method creation")

o=Outer()
i=o.Inner()
i.m1()

--------------------------
class Outer:
	def __init__(self):
		print("Outer class object Creation")
	class Inner:
		def __init__(self):
			print("Inner calss object Creation")
		class InnerInner:
			def __init__(self):
				print("InnerInner calss object Creation")
			def m1(self):
					print("InnerInner method creation")

o=Outer()
i=o.Inner()
ii=i.InnerInner()
ii.m1()
-----------------------------------------------
# program for automatic calling the all nested class inside the human class
class Human:
	def __init__(self,name):
		print("Human calss creation")
		self.name=name
		self.head=self.Head() # calling the head inside the execution of the human class 
	class Head:
		def __init__(self):
			print("Head class creation")
			self.brain=self.Brain()#calling the brain inside the execution of the head class 
		class Brain:
			def __init__(self):
				print("Brain class creation")
human = Human("Durga")
---------------------------------------
class Human:
	def __init__(self,name):
		print("Human object creation")
		self.name = name
		self.head = self.Head()

	def info(self):
		print("Hi myself: ",self.name)
		self.head.talking()
		self.head.brain.thinking()

	class Head:
		def __init__(self):
			print("Head object Creation:")
			self.brain = self.Brain()

		def talking(self):
			print("I am Talking")

		class Brain:
			def __init__(self):
				print("Brain object creation")

			def thinking(self):
				print("I am thnking")

human= Human("Durga")
human.info()
-----------------
# nested class
class Person:
	def __init__(self,name,dd,mm,yyyy):
		print('Person Object Creation')
		self.name=name
		self.dob=self.Dob(dd,mm,yyyy)
	def info(self):
		print("Name",self.name)
		self.dob.display()
	class Dob:
		
		def __init__(self,dd,mm,yyyy):
			print("DOB object creation:")
			self.dd=dd
			self.mm=mm
			self.yyyy=yyyy

		def display(self):
			print("DOB = {}/{}/{}".format(self.dd,self.mm,self.yyyy))
p = Person("durga",23,34,2999)
p.info()

---------------------------
#nested method
class  Test:

	def m1(self):
		def calc(a,b):
			print("The sum: ",a+b)
			print("The product: ",a*b)
			print("The difference:",a-b)
			print("The division:",a/b)
			print()

		calc(10,20)
		calc(100,200)
		calc(1000,2000)

t = Test()
t.m1()
-------------------------
# garbage collector

import time
class Test:
	def __init__(self):
		print("initilization of the constructor")

	def __del__(self):
		print("Initilaization of the distructor")

t= Test()
t=None
time.sleep(10)
print("end of the application")
---------------------------------------------------------
import time
class Test:
	def __init__(self):
		print("initilization of the constructor")

	def __del__(self):
		print("fulfilling the last wish and performance of destructor done")

t1=Test()
t2=t1
t3=t2
del t1
time.sleep(10)
print("Object not yet destroyed")
del t2
time.sleep(10)
print("Object not yet destroyed")
del t3
time.sleep(10)
print("End of application")
----------------------------------------
import time
class Test:
	def __init__(self):
		print("initilization of the constructor")

	def __del__(self):
		print("fulfilling the last wish and performance of destructor done")

l = [Test(),Test(),Test()]
time.sleep(10)
print("List is not required make it eligible for gc")

del l 
time.sleep(10)
print("End of application")



------------------------------
# By using composition Has-A Relationship
class Engine:
	def __init__(self):
		self.power="125kW"

	def useEngine(self):
		print("Engine Specific Functionility")

class Car:
	def __init__(self):
		self.engine=Engine()

	def useCar(self):
		print("Car require Engine functionality")
		self.engine.useEngine()
		print(self.engine.power)

c= Car()
c.useCar()
# Class car Has-a relationship with engine reference

class Car:
	def __init__(self,name,model,colour):
		self.name=name
		self.model=model
		self.colour=colour

	def getInfo(self):
		print('name {},Model {},Colour {}'.format(self.name,self.model,self.colour))


class Employee:
	def __init__(self,name,eno,car):
		self.name=name
		self.eno=eno
		self.car=car

	def empInfo(self):
		print("Employee name",self.name)
		print("Employee number",self.eno)
		print("Employee Car",end=" ")
		self.car.getInfo()

car = Car("innova","123v","gray")
emp=Employee("durga",9034637,car)
emp.empInfo()
-------------------------
class SportsNews:
	def sportsInfo(self):
		print('Sports Info-1')
		print('Sport Info-2')
		print('sport Info-3')
		print('sport Info-4')
		print('sport info-5')

class MovieNews:
	def movieInfo(self):
		print('Movie Info-1')
		print('Movie Info-2')
		print('Movie Info-3')
		print('Movie Info-4')
		print('Movie info-5')


class PoliticsNews:
	def politcsInfo(self):
		print('Politics Info-1')
		print('Politics Info-2')
		print('Politics Info-3')
		print('Politics Info-4')
		print('Politics info-5')

class DurgaNews:
	def __init__(self):
		self.sports=SportsNews()
		self.movie=MovieNews()
		self.politics=PoliticsNews()

	def getTotalNews(self):
		print("Welcome to Durga News")
		self.sports.sportsInfo()
		self.movie.movieInfo()
		self.politics.politcsInfo()

d=DurgaNews()
d.getTotalNews()
------------------------
class P:
	a=10
	def __init__(self):
		print("Parent class constructor")
		self.b=20

	def m1(self):
		print("Parent class method")

	@classmethod
	def m2(cls):
		print("class Method")

	@staticmethod
	def m3():
		print("Static Method")

class C(P):

	pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
----------------------------
# without super function() - we get the error for the parent call the construtor
class P:
	def __init__(self):
		print("Parent Constructor")
		self.a=10

class C(P):
	def __init__(self):
		print("Child constructor")
		self.b=20

c=C()
print(c.b)
print(c.a)#AttributeError: 'C' object has no attribute 'a'

-------------------------
# with super function
class P:
	def __init__(self):
		print("Parent Constructor")
		self.a=10

class C(P):
	def __init__(self):
		super().__init__()# using the super function to execute  the parent class construtor
		print("Child constructor")
		self.b=20

c=C()
print(c.b)
print(c.a)

---------------------------------------------
# Without super function 
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def eatDrink(self):
		print("Eating Biryani and Drink Beer")

class Employee(Person):
	def __init__(self,name,age,eno,esal):
		self.name=name # it is coming from the child 
		self.age=age # it is coming from child not from the parent constructor
		self.eno=eno
		self.esal=esal
	def work(self):
		print("Coding is Easy")

	def empInfo(self):
		print("Employee Name",self.name)
		print("Employee Age",self.age)
		print("Employee Number",self.eno)
		print("Employee Salary",self.esal)

e = Employee("durga",45,758568,70000)
e.eatDrink()
e.work()
e.empInfo()

--------------------
# With super function
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def eatDrink(self):
		print("Eating Biryani and Drink Beer")

class Employee(Person):
	def __init__(self,name,age,eno,esal):
		super().__init__(name,age) # using super function to execute the constructor from parent class 
		self.eno=eno
		self.esal=esal
	def work(self):
		print("Coding is Easy")

	def empInfo(self):
		print("Employee Name",self.name)
		print("Employee Age",self.age)
		print("Employee Number",self.eno)
		print("Employee Salary",self.esal)

e = Employee("durga",45,758568,70000)
e.eatDrink()
e.work()
e.empInfo()
---------------------------------------------------------
#without super()function

class Person:
	def __init__(self,name,age,hight,weight):
		self.name=name
		self.age=age
		self.heigh=height
		self.weight=weight

	def display(self):
		print("name:",self.name)
		print("age",self.age)
		print("height:",self.hight)
		print("weight:",self.weight)

class Student(Person):
	def __init__(self,name,age,hight,weight,rollno,marks):
		self.name=name
		self.age=age
		self.hight=hight
		self.weight=weight
		self.rollno=rollno
		self.marks=marks
	def display(self):
		print("name:",self.name)
		print("age:",self.age)
		print("Height:",self.hight)
		print("Weight:",self.weight)
		print("Rollno:",self.rollno)
		print("Marks:",self.marks)

c=Student("durga",23,4.5,45,45,98)
c.display()
-----------------------------------------
# the super()function
class Person:
	def __init__(self,name,age,hight,weight):
		self.name=name
		self.age=age
		self.hight=hight
		self.weight=weight

	def display(self):
		print("name:",self.name)
		print("age",self.age)
		print("height:",self.hight)
		print("weight:",self.weight)

class Student(Person):
	def __init__(self,name,age,hight,weight,rollno,marks):
		super().__init__(name,age,hight,weight)
		self.rollno=rollno
		self.marks=marks
	def display(self):
		super().display()
		print("Rollno:",self.rollno)
		print("Marks:",self.marks)

c=Student("durga",23,4.5,45,45,98)
c.display()

---------------------------------------------------------------
mini project
from abc import ABC,abstractmethod
class Account:
	def __init__(self,name,balance,min_balance):
		self.name=name
		self.balance=balance
		self.min_balance=min_balance

	def deposite(self,amount):
		self.balance +=amount

	def withdraw(self,amount):
		if self.balance-amount>=self.min_balance:
			self.balance -=amount

		else:
			print("Sorry insufficient balance")

	def printStatement(self):
		print("Account Balance: ",self.balance)
	
	@abstractmethod
	def accountInfo(self):
		pass
class SavingAccount(Account):
	def __init__(self,name,balance):
		super().__init__(name,balance,0)

	def __str__(self):
		return "It is {}'s Saving Account with balance:{}".format(self.name,self.balance)
	def accountInfo(self):
		print("It is {}'s Saving Account with balance:{} and minimum balance:{}".format(self.name,self.balance,self.min_balance))
		
class CurrentAccount(Account):
	def __init__(self,name,balance):
		super().__init__(name,balance,-1000)

	def __str__(self):
		return "It is {}'s Current Account with balance:{}".format(self.name,self.balance)
	def accountInfo(self):
		print("It is {}'s Current Account with balance:{} and minimum balance:{}".format(self.name,self.balance,self.min_balance))



'''
s = SavingAccount("Durga",10000)
print(s)
s.deposite(10000)
s.printStatement()
s.withdraw(8000)
s.printStatement()'''

c= CurrentAccount("Durgasoft",10000)
print(c)
c.deposite(5000)
c.printStatement()
c.withdraw(12000)
c.printStatement()
c.withdraw(400)
c.printStatement()
c.accountInfo()
