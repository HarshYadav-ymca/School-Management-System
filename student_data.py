import csv
with open("stud_data.csv","w",newline='') as f1:
 	thestudent=csv.writer(f1)

 	thestudent.writerow(["Adm_no","Name","Father's name","Class","House"])
 	thestudent.writerow(["001","Harsh","Pradeep kumar",7,"East"])
 	thestudent.writerow(["002","Rohit","Jaisingh",6,"West"])
 	thestudent.writerow(["003","Sourav","Subash",8,"North"])
 	thestudent.writerow(["004","Dishant","Vikram pandey",10,"North"])
 	thestudent.writerow(["005","Asit","Naveen",9,"North"])
 	thestudent.writerow(["006","Priyanshu","Naresh",5,"South"])
 	thestudent.writerow(["007","Ankur","Arvind arora",7,"East"])
 	thestudent.writerow(["008","Vicky","Virat singh",2,"South"])
 	thestudent.writerow(["009","Deepin","Ravindar kumar",1,"West"])
 	thestudent.writerow(["010","Rohan","Krishan yadav",3,"North"])
 	thestudent.writerow(["011","Rishabh","Suresh",8,"East"])
 	thestudent.writerow(["012","Subham","Purshottam Singhla",9,"South"])