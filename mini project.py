#bank system
import sys
class Customer:
	'''Customer class to describe the bank operation'''
	bankname="Durga Bank"
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance= balance

	def deposite(self,amt):
		self.balance=self.balance+amt
		print("Balance after deposite:",self.balance)

	def withdraw(self,amt):
		if amt>self.balance:
			print("insuffecient balance")
			sys.exit()
		self.balance = self.balance-amt
		print("Balance after withdraw:",self.balance)

print("Welcome To {}".format(Customer.bankname))
name = input("Enter the customer name: ")
c= Customer(name)
while True:
	print("d - Deposite/n w - Whithdraw\n e - exit")
	option = input("Enter your option :")

	if option == 'd' or option =="D":
		amt=float(input("Enter the amount: "))
		c.deposite(amt)

	elif option == "w" or option == "W":
		amt=float(input("Enter the amount:"))
		while amt % 500!=0:
			print("Amount should be multiple of 500")
			amt=float(input("Enter the amount:"))
		c.withdraw(amt)

	elif option =="e" or option =="E":
		print("Thanks for banking...")
		sys.exit()
	else:
		print("Enter The correct option: ")

----------------------------
# stdent grade
class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks

	def display(self):
		print("Hi",self.name)
		print("Your marks: ",self.marks)
		self.grade()
--------------------------------------
# Wap to track the number of object creation for a class
class Test:
	count=0
	def __init__(self):
		Test.count=Test.count +1

	@classmethod
	def get_No_Of_Object(cls):
		print("The number of object created is",cls.count)
t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()
t6=Test()

Test.get_No_Of_Object()

	def grade(self):
		if self.marks >=60:
			print("You got 1st grade!!!")
		elif self.marks >=50:
			print("you got 2nd grade!!!")
		elif self.marks >=35:
			print ("you got 3rd grade!!!")
		else:
			print("you are fail!!!")

name = input("Enter your name: ")
marks = int(input("Enter the Marks: "))
s = Student(name,marks)
s.display()
----------------------------
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

-------------------------------------
class Car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
	def getInfo(self):
		print("\t Car Name:{} \n\t Model Name:{} \n\t Car Color:{}".format(self.name,self.model,self.color))

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def eatDrink(self):
		print("Eating Biryani and Drink Beer")

class Employee(Person):
	def __init__(self,name,age,eno,esal,car):
		super().__init__(name,age) # using super function to execute the constructor from parent class 
		self.eno=eno
		self.esal=esal
		self.car=car
	def work(self):
		print("Coding is Easy")

	def empInfo(self):
		print("Employee Name",self.name)
		print("Employee Age",self.age)
		print("Employee Number",self.eno)
		print("Employee Salary",self.esal)
		print("Employee car")
		self.car.getInfo()

car= Car("toyota",'2.6v',"gray")
e = Employee("durga",45,758568,70000,car)
e.eatDrink()
e.work()
e.empInfo()
---------------------------------
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
