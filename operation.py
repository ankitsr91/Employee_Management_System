import re
import employee_management
import dbs

# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")

def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        employee_management.Add_Employ()
    Name = input("Enter Employee Name: ")
    
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        employee_management.Add_Employ()
    Email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        employee_management.Add_Employ()
    Phone_no = input("Enter Employee Phone No.: ")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = dbs.con.cursor()

    c.execute(sql, data)
    dbs.con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    employee_management.menu()

def check_employee_name(employee_name):
    sql = 'select * from empdata where Name=%s'
    c = dbs.con.cursor(buffered=True)
    data = (employee_name,)
    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_employee(employee_id):
    sql = 'select * from empdata where Id=%s'
    c = dbs.con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    sql = 'select * from empdata'
    c = dbs.con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    employee_management.menu()

def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        employee_management.menu()
    else:
        Email_Id = input("Enter Employee Email ID: ")
        if(re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Phone_no = input("Enter Employee Phone No.: ")
        if(Pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Address = input("Enter Employee Address: ")
        name = input("Enter Employee name: ")
        sql = 'UPDATE empdata set Email_Id = %s, Phone_no = %s, Address = %s, Name = %s where Id = %s'
        data = (Email_Id, Phone_no, Address, name, Id)
        c = dbs.con.cursor()
        c.execute(sql, data)

        dbs.con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        employee_management.menu()

def Promote_Employ():
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        employee_management.menu()
    else:
        Amount  = int(input("Enter Increase Salary: "))
        sql = 'select Salary from empdata where Id=%s'
        data = (Id,)
        c = dbs.con.cursor()
        
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0]+Amount
        sql = 'update empdata set Salary = %s where Id = %s'
        d = (t, Id)

        c.execute(sql, d)
        dbs.con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        employee_management.menu()

def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        employee_management.menu()
    else:
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = dbs.con.cursor()
        c.execute(sql, data)
        dbs.con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        employee_management.menu()
        
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        employee_management.menu()
    else:
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = dbs.con.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any key To Continue..")
        employee_management.menu()