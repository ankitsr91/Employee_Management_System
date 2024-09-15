from os import system
import re
from auth import authenticate_user
import operation

def menu():
    system("clear")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("clear")
        operation.Add_Employ()
    elif ch == 2:
        system("clear")
        operation.Display_Employ()
    elif ch == 3:
        system("clear")
        operation.Update_Employ()
    elif ch == 4:
        system("clear")
        operation.Promote_Employ()
    elif ch == 5:
        system("clear")
        operation.Remove_Employ()
    elif ch == 6:
        system("clear")
        operation.Search_Employ()
    elif ch == 7:
        system("clear")
        print("{:>60}".format("Have A Nice Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

def main():
    print("Welcome to the Employee Management System")
    # -------
    print("1. Log in")
    print("2. Sign up")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        if authenticate_user(input("Enter Employee Email ID: "), input("Enter Employee ID: ")):
            menu()
    elif choice == 2:
        operation.Add_Employ()
    else:
        print("Authentication Failed. Exiting...")
        exit(1)   

if __name__ == "__main__":
    main()
