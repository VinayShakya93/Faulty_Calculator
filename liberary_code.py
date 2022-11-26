print("Welcome to Liberary")
Dict = ["Ramayan", "Bhagvat Geeta", "Mahabharat", "Python","Sql"]
Cust_name = []

D = "Display books"
L = "Lend book"
A = "Donate your book"
R = "Return the book"

while True:
    op = input("Enter your name for our record: ").capitalize()
    Cust_name.append(op)
    opt = input("Enter your query:-\n"
                "press D for display books\n"
                "press L for lend book\n"
                "press A for donate your book\n"
                "press R for return book: ").capitalize()
    if opt == "D":
        print(Dict)
    elif opt == "L":
        user1 = input("Which book you want to borrow: ").capitalize()
        Dict.remove(user1)
        if user1 in Dict:
            print(f"You can take this book {user1}")
        else:
            print(f"This book is already taken by {op}\n"
                  f"Now books are available, you can choose from them: {Dict}")

    elif opt=="A":
        user = input("Enter your book name which you want to donate ").capitalize()
        Dict.append(user)
        print(f"Customer name who donate this book:- {op}")
    else:
        net = input("Enter the book name which book you want to return ").capitalize()
        Dict.append(net)
        print(f"Customer name who return this book:- {op}")
    men = input("Do you want to exit press e or continue press c: ")
    if men=="e":
        break
    elif men=="c":
        continue