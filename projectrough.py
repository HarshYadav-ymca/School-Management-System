# first i made a class of school
# display students
# add any student
# remove any student
# find a student
import shutil
import os
import csv
def clear():
	return os.system("cls")
calls=shutil.get_terminal_size().columns
class School: 
	def __init__(self,name):
		self.name=name


	def displaystudent(self):
		print()
		print((f"----****We have following students in {self.name}****----").center(calls))
		print()
		with open("C:/Users/Harsh/project.py/stud_data.csv","r",newline='') as f:
 			thestudent=csv.reader(f)
 			l=[]
 			for lines in thestudent:
 				l.append(lines)
 				print(l[0][0].ljust(20),l[0][1].ljust(20),l[0][2].ljust(20),l[0][3].ljust(20),l[0][4].ljust(20))
 				l=[]

	def addstudent(self):
		with open("C:/Users/Harsh/project.py/stud_data.csv","r",newline='') as f1:
 			thestudent_adm=csv.reader(f1)
 			l=[]
 			next(thestudent_adm)
 			for lines in thestudent_adm:
 				l.append(lines[0])
		with open("C:/Users/Harsh/project.py/stud_data.csv","a",newline='') as f:
			print()
			adm=input("Enter the adm_no. to add:")
			# flag=0
			thestudent=csv.writer(f)
			if adm  not in l:
				# flag+=1
				if len(adm)==3 :
					name=input("Enter the name to add:")
					if name.isalpha()==True:
						fathers_name=input("Enter the father's name to add:")
						if name.isalpha()==True:
							class_=int(input("Enter the `class to add:"))

							if (class_==1 or class_==2 or class_==3 or class_==4 or class_==5 or  class_==6 or class_==7 or class_==8 or class_==9 or class_==10 or class_==11 or class_==12 ):
								# flag+=1
								house=input("Enter the house to add:")

								if (house=="North" or house =='South' or house =="East" or house=="West"):
									thestudent.writerow([adm,name,fathers_name,class_,house])
									print("Data added sucessfully!!")
								else:
									
									print(" Sorry , No such house exists")
							else:
									print("Sorry! There is no such class exist in our school")
									print("Our school has class from 1 to 12 only")
						else:
							print("Please enter only alphabet ")
					else:
						print("Please enter only alphabet")
				else:
					print("Adm_no must be of three digit")
			else:
				print("Adm_no already exist")
	# 	
	def modifystuddetails(self ):
		with open("C:/Users/Harsh/project.py/stud_data.csv","r",newline='') as f1:
 			thestudent_adm=csv.reader(f1)
 			flag=0
 			l=[]
 			adm_search=input("Enter adm_no whose detail you need to modify :")
 			for lines in thestudent_adm:
 				if lines[0]==adm_search :
 					lines[1]=input("Enter name :")
 					# print(lines[1])
 					if lines[1].isalpha()==True:
 						# flag=1
		 				lines[2]=input("Enter father's name :")
		 				if lines[2].isalpha()==True:
 							# flag=1
		 					lines[3]=int(input("Enter class :"))
		 					if (lines[3]==1 or lines[3]==2 or lines[3]==3 or lines[3]==4 or lines[3]==5 or  lines[3]==6 or lines[3]==7 or lines[3]==8 or lines[3]==9 or lines[3]==10 or lines[3]==11 or lines[3]==12 ):
		 						# flag=1
		 						lines[4]=input("Enter House  :")
		 						if (lines[4]=="North" or lines[4] =='South' or lines[4] =="East" or lines[4]=="West"):
		 							print()
		 							print("Details modified sucessfully")
		 							flag=1
		 						else:
		 							flag=2
		 							break
		 					else:
		 						flag=2
		 						break
		 				else:
		 					flag=2
		 					break
		 			else:
		 				flag=2
		 				break
 				l.append(lines)
 			if flag==0:
 				print("No details found")
 			elif flag==2:
 				print("Please enter Valid Details")
 			else:
 				with open("C:/Users/Harsh/project.py/stud_data.csv","w",newline='') as f1:
 					# print(l)
 					thestudent_adm=csv.writer(f1)
 					thestudent_adm.writerows(l)
 					
		
	def findstudent(self):
		with open("C:/Users/Harsh/project.py/stud_data.csv","r",newline='') as f:
			adm=input("Enter the adm_no. to be searched:")
			flag=0
			thestudent=csv.reader(f)
			next(thestudent)
			if len(adm)==3:
				for lines in thestudent:
					# print(lines[0])
					if lines[0]==adm:
						a=lines[0]
						b=lines[1]
						c=lines[2]
						d=lines[3]
						e=lines[4]
						print()
						print("Details of student found sucessfully!!!")
						print()
						# print("[Adm_no" " ","Name","   ""Class","  ""House]")
						print("\tAdm_no" ":" + a)
						print("\tName" ":" + b)
						print("\tFather's name" ":" + c)
						print("\tClass" ":" + d)
						print("\tHouse" ":" + e)


						flag=1
						break
			else:
				flag=1
				print("Please enter only three digit admission number")
			if flag==0:
		 		print("No record found")
		 		print("Sorry this student is not from our school")
Student_data=School("RPS PUBLIC SCHOOL")		

while(True):
		clear()
		print()
		# print()
		print("******** Welome to the RPS PUBLIC SCHOOL *******".center(calls))
		print()
		print("\tEnter your choice to continue :\n")
		print("\t1. Display Students\n")
		print("\t2. Add a student in school\n")
		print("\t3. Modify a student  data\n")
		print("\t4. Find a student from school\n")

		user_choice =int(input())
		clear()
		if user_choice==1:
			Student_data.displaystudent()
		elif user_choice==2:
			Student_data.addstudent()
		elif user_choice==3:
			Student_data.modifystuddetails()
		elif user_choice==4:
			Student_data.findstudent()

		
		else:
			print("Not a valid option!")
		print()
		print("Press c to Continue and q to Quit")
		user_choice2=input()
		if user_choice2=="c":
			continue
		elif user_choice2=="q":
			clear()
			exit()
			