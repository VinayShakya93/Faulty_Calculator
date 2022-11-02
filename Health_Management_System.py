# Health Management System

def timedate():
    import datetime
    return datetime.datetime.now()
print("Welcome to Health Management System")
def take(K):
    if K == 1:
        user = int(input("Choose your option:- Press 1 for Exercise, Press 2 for Food\n"))
        if user==1:
            Person = input("Enter your Exercise name\n")
            with open ("Vinay_Ex.txt", "a") as pk:
                pk.write(str([str(timedate())]) + "-" + Person + "\n")
                print("Successfully written")
        elif user==2:
            Person = input("Enter your Food name\n")
            with open("Vinay_Food.txt", "a") as pk:
                pk.write(str([str(timedate())]) + "-" + Person + "\n")
                print("Successfully written")
    elif K==2:
        user = int(input("Choose your option:- Press 1 for Exercise, Press 2 for Food\n"))
        if user==1:
            Person = input("Enter your Exercise name\n")
            with open ("Ashish_Ex.txt", "a") as pk:
                pk.write(str([str(timedate())]) + "-" + Person + "\n")
                print("Successfully written")
        elif user==2:
            Person = input("Enter your Food name\n")
            with open("Ashish_Food.txt", "a") as pk:
                pk.write(str([str(timedate())]) + "-" + Person + "\n")
                print("Successfully written")
    elif K==3:
        user = int(input("Choose your option:- Press 1 for Exercise, Press 2 for Food\n"))
        if user == 1:
            Person = input("Enter your Exercise name\n")
            with open("Avichal_Ex.txt", "a") as pk:
                pk.write(str([str(timedate())]) + "-" + Person + "\n")
                print("Successfully written")
        elif user == 2:
            Person = input("Enter your Food name\n")
            with open("Avichal_Food.txt", "a") as pk:
                pk.write(str([str(timedate())]) + "-" + Person + "\n")
                print("Successfully written")
    else:
        print("Please select valid input: 1(Vinay),2(Ashish),3(Avichal)")
def retrieve(T):
    if T==1:
        user = int(input("Choose your option:- Press 1 for Exercise, Press 2 for Food\n"))
        if user ==1:
            with open("Vinay_Ex.txt") as pk:
                for i in pk:
                    print(i,end=" ")
        elif user==2:
                with open("Vinay_Food.txt") as pk:
                    for i in pk:
                        print(i, end=" ")
    elif T==2:
        user = int(input("Choose your option:- Press 1 for Exercise, Press 2 for Food\n"))
        if user == 1:
            with open("Ashish_Ex.txt") as pk:
                for i in pk:
                    print(i, end=" ")
        elif user == 2:
            with open("Ashish_Food.txt") as pk:
                for i in pk:
                    print(i, end=" ")
    elif T==3:
        user = int(input("Choose your option:- Press 1 for Exercise, Press 2 for Food\n"))
        if user == 1:
            with open("Avichal_Ex.txt") as pk:
                for i in pk:
                    print(i, end=" ")
        elif user == 2:
            with open("Avichal_Food.txt") as pk:
                for i in pk:
                    print(i, end=" ")
    else:
        print("Please select valid input: 1(Vinay),2(Ashish),3(Avichal)")
V = int(input("Please choose 1 for log or choose 2 for retrieve\n"))
if V==1:
    S = int(input(" press 1 for Vinay: \n press 2 for Ahsish: \n press 3 for Avichal: "))
    take(S)
else:
    S = int(input("press 1 for Vinay: \n, press 2 for Ahsish: \n press 3 for Avichal: "))
    retrieve(S)



