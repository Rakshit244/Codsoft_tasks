cbook=[["Tim",4658468,"tim6546@gmail.com","hello"]]
def display():
    if len(cbook)==0:
        print("No Contact")
    else:
        for i in cbook:
            print("Name:",i[0],"Phone Number:",i[1],"Email:",i[2],"Address:",i[3])

def addcontact():
    name=input("Enter Name:")
    phone=int(input("Enter Phone Number:"))
    email=input("Enter Email:")
    address=input("Enter Address:")
    cbook.append([name,phone,email,address])

while True:
    print("Menu\n1.Add Contact\n2.View Contact\n3.Search Contact\n4.Update Contact\n5.Delete Contact\n6.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        addcontact()
    elif choice==2:
        display()
    elif choice==3:
        name=input("Enter Name:")
        for i in cbook:
            if i[0]==name:
                print("Name:", i[0], "Phone Number:", i[1], "Email:", i[2], "Address:", i[3])
                print("Found!")
                break
        else:
            print("Invalid Choice")
    elif choice==4:
        name=input("Enter Name:")
        for i in cbook:
            if i[0]==name:
                print("Name:", i[0], "Phone Number:", i[1], "Email:", i[2],"Address:", i[3])
                i[0] = input("Enter Name:")
                i[1] = int(input("Enter Phone Number:"))
                i[2] = input("Enter Email:")
                i[3] = input("Enter Address:")
                break
        else:
            print("Invalid Choice")
    elif choice==5:
        name=input("Enter Name:")
        for i in cbook:
            if i[0]==name:
                cbook.remove(i)
                print("Deleted!")
                break
        else:
            print("Invalid Choice")
    elif choice==6:
        exit()