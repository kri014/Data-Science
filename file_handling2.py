f = open("abc.txt",'r')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
-------------------------------
###output
File name: abc.txt
File Mode: r
File readable: True
File Writeable: False
File closed: False
File closed: True
---------------------------------------
f = open("abc.txt")
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
---------------------------
# output
File name: abc.txt
File Mode: r
File readable: True
File Writeable: False
File closed: False
File closed: True
-------------------------------------
# in write mode if file already availble
f = open("abc.txt",'w') # will overwrite in the existing file
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
-------------------------------------
output
File name: abc.txt
File Mode: w
File readable: False
File Writeable: True
File closed: False
File closed: True
-------------------------------
# new file created if file not exist
f = open("abc_ede.txt",'w')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
----------------------
File name: abc_ede.txt
File Mode: w
File readable: False
File Writeable: True
File closed: False
File closed: True
------------------------------------
# append mode
f = open("abc_ed.txt",'a')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
------------------------------------
File name: abc_ed.txt
File Mode: a
File readable: False
File Writeable: True
File closed: False
File closed: True
--------------------------------------
f = open("abc_ed.txt",'r+')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
-------------------------------------
File name: abc_ed.txt
File Mode: r+
File readable: True
File Writeable: True
File closed: False
File closed: True
-------------------------
f = open("abc_ed.txt",'a+')
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
----------------------------------
File name: abc_ed.txt
File Mode: a+
File readable: True
File Writeable: True
File closed: False
File closed: True
-----------------------------------------
f = open("abc_ed.txt",'x') # show error if file exist
print("File name:",f.name)
print("File Mode:",f.mode)
print("File readable:",f.readable())
print("File Writeable:",f.writable())
print("File closed:",f.closed)
f.close()
print("File closed:",f.closed)
--------------------------------------------

Traceback (most recent call last):
  File "test.py", line 1, in <module>
    f = open("abc_ed.txt",'x') # show error if file exist
FileExistsError: [Errno 17] File exists: 'abc_ed.txt'
-------------
f= open('abc.txt','a')
f.write('krishna\n')
f.write('deepak\n')
f.write('Pushpa')

print("The name has been written in the file")
f.close()

-----------------
f= open('abc.txt','a')
l=["krishna\n","mukesh\n","atul\n","rohan"]
for s in l:
	f.write(s)
print("The name has been written in the file")
f.close()
