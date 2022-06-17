import shutil
calls=shutil.get_terminal_size().columns
import sqlite3 as s3
conn = s3.connect("Stude_data.db")
cur = conn.cursor()
# Query1 = """
# 		CREATE TABLE IF NOT EXISTS student_data(
# 			Adm_no integer  PRIMARY KEY AUTOINCREMENT,
# 			Name VARCHAR(40) NOT NULL,
# 			Fathers_name VARCHAR(40) NOT NULL,
# 			Class INT, 
# 			House VARCHAR(40) NOT NULL
# 			);
#  			"""
# cur.execute(Query1)
# cur.fetchall()
# conn.commit()
# # #
# Query2="""
# 		INSERT INTO student_data(Name,Fathers_name,Class,House)
# 		VALUES ("Sunny","Dharmender",12,"East");
# 		"""
# cur.execute(Query2)
# # cur.fetchall()
# conn.commit()
# conn.close()

# Query3="""
#  		DROP TABLE student_data
# 		"""
#  Query3="""
# 		SELECT * FROM student_data


# 		"""
# cur.execute(Query3)
# print(cur.fetchall())


def display():
	Query3="""
 				SELECT * FROM student_data order by Adm_no;


			"""
	cur.execute(Query3)
	print("Adm_no.","".ljust(4),"Name".ljust(20),"Father's name".ljust(20),"".ljust(10),"Class","".ljust(5),"House".ljust(10))
	print()
	for row in cur.fetchall():
		print(row[0],"".ljust(10),row[1].ljust(20),row[2].ljust(20),"".ljust(10),row[3],"".ljust(10),row[4].ljust(10))
	# conn.commit()
	# print("Adm_no.\t\t\t\t","Name\t\t\t\t","Father's name\t\t\t\t","Class\t\t\t\t","House\t\t\t\t")
	# print()
	# for row in cur.fetchall():
	# 	print(row[0],"\t\t\t\t\t",row[1],"\t\t\t\t",row[2],"\t\t\t\t\t\t",row[3],"\t\t\t\t",row[4],"\t\t\t\t")

# display()


def add(a,b,c,d): 
	Query2 ="""
			INSERT INTO student_data(Name,Fathers_name,Class,House)
			VALUES(?,?,?,?);
			"""
	cur.execute(Query2,(a,b,c,d))
	conn.commit()

def update_data(a,b,c,d,e):
	Query2= """
			UPDATE student_data
			SET Name = ?, Fathers_name= ?,Class =? ,House=?
			WHERE Adm_no = ?;
			"""
	cur.execute(Query2,(a,b,c,d,e))
	conn.commit()


def admission_no_search(Adm__no):
	Query3 ="""
			SELECT * FROM student_data where Adm_no = ? ;
			"""
	cur.execute(Query3,(Adm__no,))
	row=cur.fetchone()
	a=row[0]
	b=row[1]
	c=row[2]	
	d=row[3]	
	e=row[4]
	print("\tData found Sucessfully!!!")
	print()
	print("\tAdmission no. : ", a)
	print()
	print("\tName :"  + b)
	print()
	print("\tFather's name :" + c)
	print()
	print("\tClass :" , d)
	print()		
	print("\tHouse :"  + e)
	print()


# admission_no_search(1)




# # Query2="""
# # 			SELECT * FROM student_data where Adm_no = {a}; 
# # 			""".format(a=10)
# # cur.execute(Query2)
# # rows=cur.fetchone()
# # print(rows)


def delete(Adm__no):
	Query3="""
		DELETE FROM student_data WHERE Adm_no = ?;
		"""
	cur.execute(Query3,(Adm__no,))
	row=cur.fetchone()
# delete(ad)