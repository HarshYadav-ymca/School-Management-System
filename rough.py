# import shutil
# import os
# import csv
# def clear():
# 	return os.system("cls")
# calls=shutil.get_terminal_size().columns
# with open("C:/Users/Harsh/project.py/stud_data.csv","r",newline='') as f:
#  			thestudent=csv.reader(f)
 			# l=[]
 			# for lines in thestudent:
 			# 	l.append(lines)
 			# 	print(l[0][0].ljust(10),l[0][1].ljust(10),l[0][2].ljust(10),l[0][3].ljust(10))
 			# 	l=[]
 			# adm=input("enter")
 			# for lines in thestudent:
 			# 	if l[0]==adm:

# a="hars1"
# print(a.isalpha)
# a=5
# b=5
# if a==5:
# 	print("hi")
# if a==5:
# 	print("Sorry")
# A="""
# 	harsh
# 	"""
# print(A)
# b = "Hello, World!"
# print(b[-])
# a="Hello World!"
# print(a.upper())
# a = "hello, WORLD!"
# print(a.split("e"))
# print(a.capitalize())
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]

# thislist.sort(key = myfunc)

# print(thislist)
# print(abs(23-45))
# a=[]
# b=a.append([1])
# print(b)
# a=[1,2,3]
# b=list(a)
# print(b)

import projectdb as p
from tkinter import *

scr=Tk()
scr.title("School")
scr.geometry("500x300+500+200")
def fun():
	p.display_student()
btn1=Button(scr,text="Button",command=fun,bd=10)
btn1.pack()
name1=Label(scr,text="I am Label1")
# name1.conf
name1.pack()


# scr.resizable("False")
scr.mainloop()
btn(scr,"1000",fun,5)