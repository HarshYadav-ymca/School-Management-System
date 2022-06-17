# first i made a class of school
# display students
# add any student
# remove any student
# find a student

class School: 
	def __init__(self,stud_name_admis_no,name):
		self.studentstud_name_admis_no=stud_name_admis_no
		self.name=name


	def displaystudent(self):
		print(f"----**We have following students in {self.name}**----")
		for student,admis_no in self.studentstud_name_admis_no.items():
			print(student.ljust(0)   ,    admis_no.ljust(15))

	def addstudent(self,student,admis_no):
		self.studentstud_name_admis_no[student]=rollno
		print({"Student has been added to the student list"})
		# self.studentdictionary.update({student:rollno})

	def removestudent(self,student ):
		
		self.studentstud_name_admis_no.pop(student)
		print("Student data remove sucessfully")

	def findstudent(self,student):
	 	if student in self.studentstud_name_admis_no.keys():
	 		print("Student is from our school")
	 	else:
	 		print("No record found")
	 		print("Sorry this student is not from our school")

student=School({"Harsh":"1","Rohan":"2","Sorav":"3","Rohit":"4","Ankur":"5","Priyanshu":"6","Vicky":"7","Rishabh":"8","Asit":"9","Bhavya":"10","Subham":"11","Ankit":"12","Rithik":"13","Dishant":"14"},"RPS PUBLIC SCHOOL")

while(True):
		print("************************************************")
		print("******** Welome to the RPS PUBLIC SCHOOL *******")
		print("************************************************")
		print("Enter your choice to continue")
		print("1. Display Students")
		print("2. Add a student in school")
		print("3. Remove a student from school")
		print("4. Find a student from school")

		user_choice =int(input())

		if user_choice==1:
			student.displaystudent()

		elif user_choice==2:
			student=input("Enter the name of student yo want to add:")
			rollno=input("Enter the rollno of student:")
			student.addstudent(student,admis_no)

		elif user_choice==3:
			student=input("Enter the name of student yo want to remove:")
			student.removestudent(student)

		elif user_choice==4:
			student=input("Enter the name of student yo want to find:")
			student.findstudent(student)

		else:
			print("Not a valid option!")

		print("Press c to Continue and q to Quit")
		user_choice2=input()
		if user_choice2=="c":
			continue
		elif user_choice2=="q":
			exit()
