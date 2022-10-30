print("                      EMPLOYEE MANAGEMENT SYSTEM                        ")


# importing mysql connector
import mysql.connector
#importing pickle
import pickle

#making connection
try:
        con =mysql.connector.connect (host = "localhost" , user = "root" , password = "jeff1234")
except:
        print("Connection Error")
        
#allows row-by-row processing of the result sets.    
cur= con.cursor() 

cur.execute('drop database  emp')

#creating database
cur.execute('create database  emp')

cur.execute('use emp')

#creating table
cur.execute("CREATE TABLE empd(Id int Primary key,Name varchar(15),Post varchar(15),Salary int)")
#inserting values
cur.execute("INSERT INTO empd VALUES(1,'john','manager',200000)")
cur.execute("INSERT INTO empd VALUES(2,'maria','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(3,'guss','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(4,'laia','manager',2000)")
cur.execute("INSERT INTO empd VALUES(5,'jeffy','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(6,'dane','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(7,'circe','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(8,'donna','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(9,'harvey','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(10,'mike','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(11,'jake','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(12,'sheldon','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(13,'leonard','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(14,'penny','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(15,'amy','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(16,'bernadette','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(17,'chris','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(18,'greg','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(19,'hermione','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(20,'manny','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(21,'tommy','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(22,'manju','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(23,'susan','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(24,'rachel','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(25,'ana','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(26,'jacob','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(27,'adarsh','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(28,'george','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(29,'jeremy','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(30,'rose','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(31,'ryan','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(32,'mary','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(33,'sam','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(34,'kimberly','clerk',10000)")
cur.execute("INSERT INTO empd VALUES(35,'zane','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(36,'abel','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(37,'alex','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(38,'vinod','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(39,'piper','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(40,'annabeth','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(42,'marilyn','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(43,'jenifer','manager',200000)")
cur.execute("INSERT INTO empd VALUES(44,'scarlett','analyst',30000)")
cur.execute("INSERT INTO empd VALUES(45,'khan','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(46,'smith','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(47,'west','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(48,'lynn','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(49,'ethan','salesman',25000)")
cur.execute("INSERT INTO empd VALUES(50,'geoffrey','analyst',30000)")


con.commit()#to commit the inserted tables to the table

# menu function to display menu
def menu():
 try:
    
    while True:
        
                print("Welcome to Employee Management Record")
                print("Press ")
                print("1 To Search Employee")
                print("2 To Add Employee")
                print("3 To Remove Employee ")
                print("4 To Increase Employee salary ")
                print("5 To Display Employees")
                print("6 To Export list of Employees")
                print("7 to Exit")
                c = int(input("Enter your Choice "))
                if c == 1:
                    search_employ()
                if c == 2:
                    Add_Employ()
                elif c == 3:
                    Remove_Employ()
                elif c == 4:
                    Promote_Employee()
                elif c == 5:
                    Display_Employees()
                elif c == 6:
                    export()
                elif c == 7:
                    exit(0)
                else:
                    print("Invalid Choice")
    
 except ValueError:
     print("Enter correct value")
     menu()
    
def search_employ():
 try:
   
            k=int(input("enter id"))
            q="select * from empd where Id=%s"
            tu=(k,)
            cur.execute(q,tu)
            data=cur.fetchall()
            for row in data:
                if row[0]==k:
                    print("Id :" ,row[0]," Name :" ,row[1]," Post :",row[2]," Salary :",row[3])
                    menu()
                else:
                    print("Doesnt exist")
                    pass
                    menu()
 except ValueError:
           print("Enter correct value")
# Function to mAdd_Employee
def Add_Employ():
 try:
    Id = input("Enter Employee Id : ")
     
    # Checking if Employee with given Id
    # Already Exist or Not
    if(check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
         
    else:
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        data = (Id, Name, Post, Salary)
     
        # Inserting Employee details in
        # the Employee Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Added Successfully ")
        menu()
 except  :
         print("enter correct value!!!")
 
# Function to Promote Employee
def Promote_Employee():
 try:
    Id = int(input("Enter Employ's Id"))
     
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
         
        # Query to Fetch Salary of Employee
        # with given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
         
        # Query to Update Salary of Employee with
        # given Id
        sql = 'update empd set salary=%s where id=%s'
        d = (t, Id)
         
        # Executing the SQL Query
        c.execute(sql, d)
         
        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        menu()
 except ValueError:
         print("Enter correct value")
# Function to Remove Employee with given Id
def Remove_Employ():
 try:
    Id = input("Enter Employee Id : ")
     
    # Checking if Employee with given Id Exist
    # or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
         
        # Query to Delete Employee from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Removed")
        menu()
 except ValueError:
         print("Enter correct value")
 
 
# Function To Check if Employee with
# given Id Exist or Not
def check_employee(employee_id):
     
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'
     
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
     
    # Executing the SQL Query
    c.execute(sql, data)
     
    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 
# Function to Display All Employees
# from Employee Table
def Display_Employees():
     
    # query to select all rows from
    # Employee Table
    sql = 'select * from empd'
    c = con.cursor()
     
    # Executing the SQL Query
    c.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    print()
    print("Processing please wait....")
    import time
    #importing module time
    time.sleep(3)
    print()
    print("Printing results....")
    time.sleep(2)
    print()
    for i in r:
        print(" Id :    ",   i[0]   ,     " Name : ", i[1] ,    " Post : "  , i[2] ,   " Salary : "  , i[3] )
       
    menu()
 
def export():
    bfile=open('employeemg.dat','wb')
    cur.execute('select * from empd')
    rows=cur.fetchall()
    for i in rows:
        k=list(i)
        pickle.dump(k,bfile) #Writing to binary file
    print('\nEmployees successfully exported to File!')
    bfile.close()
    try:
        bfile=open('employeemg.dat','rb')
        print('\n*****EMPLOYEES IN EXPORTED FILE*****:')
        while True:
            g=pickle.load(bfile) #Reading from binary file
            print(" Id :    ",   g[0]   ,     " Name : ", g[1] ,    " Post : "  , g[2] ,   " Salary : "  , g[3])
    except EOFError:
        pass
        menu()

# Calling menu function
menu()
