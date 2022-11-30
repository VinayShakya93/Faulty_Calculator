# creating online liberary using oops method
print("Welcome to Vinay's Liberary")
while True:
    user = input("Enter your name: ").capitalize()
    books_stock = ["Mahabharat", "Ramayana", "Bhagwat Geeta", " Ramcharitmanas", "Garg Sahinta", "Python", "Sql", "C++","C"]
    lend = {}
    class Liberary:
        def __init__(self, bname, lname):
            self.bname = bname
            self.lname = lname
        @property
        def display(self):
            return f"Welcome! Available books are:-\n{self.bname}\n"
        def lend_book(self):
            search = input("Which book you want, Type here!!").capitalize()
            if search in books_stock and search not in lend.keys():
                print(books_stock)
                claim = input("If book is available. Press 1 for claim, else press 0: ")
                if claim == 1:
                    books_stock.remove(search)
                    lend.update({search:user})
                    return f"Thanks for claiming {search}, Enjoy your book"
                elif claim ==0:
                    return "Thank You"
            elif search not in books_stock:
                return f"Opps!! {search} is not available right now. Try after few days"
            elif search in "books_stock" and search in lend.keys():
                return f"{search} is available but {lend.get(search)} is already lended this book."
        def add_book(self):
            add = input("Enter book's name you want to donate: ").capitalize()
            con = input("Press 1 for confirm else press 0: ")
            if con==1:
                books_stock.append(add)
                return f"Hey! Team Mr.{user} donate his book '{add}' Congrachulations Sir "
            elif con ==0:
                return "Its okk!  Visit again!!"
        def return_book(self):
            ret = input("Enter the book's name which You want to return: ").capitalize()
            if ret in lend.keys():
                con = input("Press y for confirm else press n: ").capitalize().capitalize()
                if con=="y":
                    del lend[ret]
                    return f"Thanks for your responsibility.\n {lend.items()}\n\n"
                elif con=="n":
                    return "its okk!!\n"
    vinay_liberary = Liberary(books_stock, "Vinay's Liberary")
    def command():
        while 1:
            print("How may i help you.\n"
                  "Press 1 to display book's stock\n"
                  "Press 2 to lend book\n"
                  "Press 3 to donate your book\n"
                  "Press 4 to Return book: ")
            opt = int(input("Enter your Query: "))
            if opt==1:
                print(vinay_liberary.display)
            elif opt==2:
                print(vinay_liberary.lend_book())
            elif opt==3:
                print(vinay_liberary.add_book())
            elif opt==4:
                print(vinay_liberary.return_book())
            else:
                print("Invalid Input!!! Try Again")
            c =int(input("press 1 to Continue or exit press 0"))
            if c==1:
                continue
            elif c==0:
                break
    command()
