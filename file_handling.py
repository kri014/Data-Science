# file handling concept
# read mode 
f = open("abc.txt",'r')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)

# read in default mode 
f = open("abc.txt")
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)

# in write mode if file already availble
f = open("abc.txt",'w') # will overwrite in the existing file
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)

# new file created if file not exist
f = open("abc_ed.txt",'w')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
# append mode
f = open("abc_ed.txt",'a')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
------
f = open("abc_ed.txt",'r+')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
---------
f = open("abc_ed.txt",'a+')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
-----------------------
f = open("abc_ed.txt",'x') # show error if file exist
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
-------------------------
# to write somthing un the acb.txt file
# everytime when it open it will overwrite the text
f = open("abc.txt","w")
f.write("Durga\n")
f.write("Software\n")
f.write("solution\n")
print("Data written to the file is sucessful")

f.close()


----
# evertime it will add the text as the file execute
f = open("abc.txt","a")
f.write("Durga\n")
f.write("Software\n")
f.write("solution\n")
print("Data written to the file is sucessful")

f.close()
---------------
# list of lines 
f = open("abc.txt","w")
l =["sunny\n","binny\n","chinny\n","vinny"]
f.writelines(l)
print("Data written to the file is sucessful")

f.close()
---------------------
# to open th file which is not present in same directory 
f = open("F:\\abc.txt","w")# we have to provide the path
l =["sunny\n","binny\n","chinny\n","vinny"]
f.writelines(l)
print("Data written to the file is sucessful")

f.close()
-------------------------------
# dynamic file name and the data in the file  
f_name= input("Create a file name")
f  = open("F:\\student_data\\"+f_name,"w")# file name is concatanate with the folder in directory
while True:
	data= input("Enter the data ")
	f.write(data)
	option = input("Do you want to write more data :[yes:no]")
	if option.lower()=="no":
		break
print("Data added sucessfully")
f.close()
------------------
f_name= input("Create a file name")

while True:
	f  = open("F:\\student_data\\"+f_name,"w") # here every time the input data will update 
	data= input("Enter the data ")
	f.write(data)
	option = input("Do you want to write more data :[yes:no]")
	if option.lower()=="no":
		break
print("Data added sucessfully")
f.close()

-----------------------------------
f_name= input("Create a file name")

while True:
	f  = open("F:\\student_data\\"+f_name,"a") # here every time the input data will added in append  
	data= input("Enter the data ")
	f.write(data)
	option = input("Do you want to write more data :[yes:no]")
	if option.lower()=="no":
		break
print("Data added sucessfully")
f.close()
------------------------------------------
# How to read data from file
# read() - to read all the data 
f = open("abc.txt","r")
word = f.read()
print(word)
# read(n)-  to read only n chartacter
f = open("abc.txt","r")
word = f.read(6) # Durgas
print(word)
# readline()
f = open("abc.txt","r")
word = f.readline() # Durgas
print(word)
#readlines() = read only lines in the list 
# it form a list of strings 
f = open("abc.txt","r")
word = f.readlines() # Durgas
print(word)

--------------------------
# file handling concept
# readline()
f = open("abc.txt","r")
word = f.readline()
print(word)
word = f.readline()
print(word)
word = f.readline()
print(word)
f.close()
'''
Durgasoftware solution

sunny

bunny
'''
# here end line is '\n' so extra line is coming

# output without the extra line 
f = open("abc.txt","r")
word = f.readline()
print(word,end='')
word = f.readline()
print(word,end='')
word = f.readline()
print(word,end='')
f.close()
--------------------------------------
# reading the text in abcd file
f = open("abcd.txt","r")
line= f.readline()
while line!="":
		print(line,end ='')
		line=f.readline()
f.close()
----------------------
# ignoring all the lines in the which is having the space
f = open("abcd.txt","r")
line= f.readline()
while line!="":
	if line!="\n":
		print(line,end ='')
	line=f.readline()
f.close()
---------------------------------
# readlines()
f = open('abc.txt','r')
lines=f.readlines()# list of string
print(lines)
for line in lines:
	print(line,end="")

f.close()
-------------------------------
# read data from input file and copied in another output file
f1=open("input.txt","r")
f2=open("output.txt","w")
read=f1.read()
f2.write(read)
f1.close()
f2.close()
print("data are copied")