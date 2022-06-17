import shutil
import os
import csv
import sqlite3 as sq
import data as db
def clear():
	return os.system("cls")
calls=shutil.get_terminal_size().columns
class School: 
	def __init__(self,name):
		self.name=name


	def display_student(self):
		print()
		print((f"----****We have following students in {self.name}****----").center(calls))
		print()
		db.display()
	
	

	def add_student(self):
				
		Name_=input("Enter the name to add:")
		if Name_.isalpha()==False:
			print()
			print("Enter Valid Name")
			Name_=input("\tEnter the name to add:")
		else:
			pass
		Fathers_name_=input("Enter the father's name to add:")
		if Fathers_name_.isalpha()==False:
			print() 
			print("Enter Valid Father's Name")
			Fathers_name_=input("\tEnter the name to add again:")
		else:
			pass
			Class_=input("\tEnter the `class to add:")
			if Class_.isdigit()==False:
				print()
				print("\tEnter Valid Class in Numbers")
				Class_=input("\tEnter the `class to add again:")
			else:
				if int(Class_) not in range(1,13):
					print()
					print("\tEnter Valid Class in between 1-12")
					Class_=int(input("\tEnter the `class to add again:"))
			House_name=input("\tEnter the house to update:")
			if  House_name.isalpha()==False:
				print()
				print("\tEnter Valid House Name")
				House_name=input("\tEnter the house to add again:")
			else:
				if House_name not in ["East","West","North","South"]:
					print()
					print("Enter Valid House Name")
					House_name=input("\tEnter the house to add again:")

			db.add(Name_,Fathers_name_,Class_,House_name)
			print()
			print("Data added sucessfully")
						
	def modify_student_details(self ):
		try:
			Admission_no=input("\tEnter the admission number of studet whom data you want to update:")
			if Admission_no.isdigit()==False:
				print()
				print("Enter Valid Admission No")
				Admission_no=input("\tEnter the admission number of studet whom data you want to update:")
			else:
				pass
			Admission_no=int(Admission_no)
			db.admission_no_search(Admission_no)
			Name_=input("\tEnter the name to update:")
			if Name_.isalpha()==False:
				print()
				print("Enter Valid Name")
				Name_=input("\tEnter the name to update:")
			else:
				pass
			Fathers_name_=input("\tEnter the father's name to update:")
			if Fathers_name_.isalpha()==False:
				print()
				print("Enter Valid Father's Name")
				Fathers_name_=input("\tEnter the name to update:")
			else:
				pass
			Class_=input("\tEnter the `class to update:")
			if Class_.isdigit()==False:
				print()
				print("\tEnter Valid Class in Numbers")
				Class_=input("\tEnter the `class to update:")
			else:
				if int(Class_) not in range(1,13):
					print()
					print("\tEnter Valid Class in between 1-12")
					Class_=int(input("\tEnter the `class to update:"))									
			House_name=input("\tEnter the house to update:")
			if  House_name.isalpha()==False:
				print()
				print("\tEnter Valid House Name")
				House_name=input("\tEnter the house to update again:")
			else:
				if House_name not in ["East","West","North","South"]:
					print()
					print("Enter Valid House Name")
					House_name=input("\tEnter the house to update again:")
			db.update_data(Name_,Fathers_name_,Class_,House_name,Admission_no)
			print()
			print("Data updated sucessfully")
		except Exception as e:
			print("Can not connect")
		
	def find_student(self):
		try:
			Admission__no=int(input("Enter the adm_no to find :"))
			db.admission_no_search(Admission__no)
		except Exception as e:
			print("No such Admission number student  exists in our school ")

	def Delete_data(self):	
		Admission__no=int(input("Enter the admission number to delete:"))
		print()
		print("Data deleted sucessfully")
		db.delete(Admission__no)
if __name__ == '__main__':
	Student_data1=School("RPS PUBLIC SCHOOL")		
	while True:
		clear()
		print()
		print("******** Welome to the RPS PUBLIC SCHOOL *******".center(calls))
		print()
		print("\tEnter your choice to continue :\n")
		print("\t1. Display Students\n")
		print("\t2. Add a student in school\n")
		print("\t3. Modify a student  data\n")
		print("\t4. Find a student from school\n")
		print("\t5. Delete student data \n")

		user_choice =int(input())
		clear()
		if user_choice==1:
			Student_data1.display_student()
		elif user_choice==2:
			Student_data1.add_student()
		elif user_choice==3:
			Student_data1.modify_student_details()
		elif user_choice==4:
			Student_data1.find_student()
		elif user_choice==5:
			Student_data1.Delete_data()


			
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
				