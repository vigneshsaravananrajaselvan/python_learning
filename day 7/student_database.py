database={}

while True:

    print("\n===== MENU =====")

    print("1.Add Student")
    print("2.Display Students")
    print("3.Update Marks")
    print("4.Delete Student")
    print("5.Exit")

    choice=int(input("Enter Choice : "))

    if choice==1:

        roll=input("Enter Roll Number : ")

        name=input("Enter Name : ")

        mark=int(input("Enter Marks : "))

        database[roll]={
            "Name":name,
            "Marks":mark
        }

        print("Student Added Successfully")

    elif choice==2:

        if len(database)==0:
            print("No Student Found")

        else:

            for roll,data in database.items():

                print("--------------------")
                print("Roll :",roll)
                print("Name :",data["Name"])
                print("Marks :",data["Marks"])

    elif choice==3:

        roll=input("Enter Roll Number : ")

        if roll in database:

            new_mark=int(input("Enter New Marks : "))

            database[roll]["Marks"]=new_mark

            print("Marks Updated Successfully")

        else:

            print("Student Not Found")

    elif choice==4:

        roll=input("Enter Roll Number : ")

        if roll in database:

            del database[roll]

            print("Student Deleted Successfully")

        else:

            print("Student Not Found")

    elif choice==5:

        print("Thank You!")

        break

    else:

        print("Invalid Choice")