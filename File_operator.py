print("Welcome to our new project File_Operator :)")

class New_entry:
    
    def __init__(self,N_Entry):
        self.N_Entry = N_Entry

        with open("demo.txt","a") as file:
            file.write(N_Entry + "\n")

        print("Entry added successfullly :)")

class View_all_entry:
    
    def __init__(self):
            self.filename = "demo.txt"

    def reader(self):
        file = open("demo.txt","r")

        lines = file.readlines()
            
        for i in lines:
            print(i)


class Clear_all_entries:

    def __init__(self):
        self.filename = "demo.txt"
    def c_E(self):
        Confirmation = input("\nAre youe about deleting All entries(Yes/No) : \n")
        if Confirmation == "Yes" or "yes":
            with open("demo.txt") as file:
                file.write("")
        elif Confirmation == "No" or "no":
            print("Entries are safe :)")
        else:
            print("Invalid choice.")

class Search_Entry:
    def __init__(self):
        self.filename = "demo.txt"
    def srch(self):
        
        with open("demo.txt","r") as file:
            lines = file.readlines()
            kwrd = input("\nEnter a keyword which you want to found : \n")
            for line in lines:
                if kwrd in line:
                    print("---------------")
                    print(f"[{now}]")
                    print(line)


import datetime

now = datetime.datetime.now()

while True:
     
    print("Enter 1 to Add Entry.")
    print("Enter 2 to View all Entries.")
    print("Enter 3 to Search entry.")
    print("Enter 4 to Clear all entry.")
    print("Enter 0 to exit the programme.")

    Choice = int(input("Enter your Choice here : "))

    if Choice == 1:
          
        new_entry = input("Enter your Journal entry : ")

        obj = New_entry(new_entry)
        print("\n New entry added succesfully :)\n")

    elif Choice == 2:
        print("\nHere are the all entries :)\n")
        obj2 = View_all_entry()
        obj2.reader()
        print(f"[{now}]\n")
       

    elif Choice == 3:
        obj3 = Search_Entry()
        obj3.srch()
        print(f"[{now}]\n")


    elif Choice == 4:
        obj4 = Clear_all_entries()
        obj4.c_E()
        print(f"[{now}]\n")


    elif Choice == 0:
        print("Thanks for visiting our Project :)")
        print(f"[{now}]\n")

        break
    else:
        print("Your entered Choice is invalid :(")

