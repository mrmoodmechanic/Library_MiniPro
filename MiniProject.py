#mini project - library

class library:
    def __init__(self, list):
        self.BookList=list
        self.lenddict={}

    def DisplayBook(self):
        print(f"Following are the books in the library :")
        for item in self.BookList:
                print(f"-{item}")


    def LendBook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Updated the book into list, You can take the book")
        else:
            print(f"The book is not available at the time. It is taken by {self.lenddict[book]}")



    def ReturnBook(self,book):
        self.lenddict.pop(book)
        print("Thanks for return")


    def AddBook(self,book):
        self.BookList.append(book)
        print("Thanks for adding new book")

if __name__=='__main__':
    suraj=library(['Alchemist','Rich dad & poor dad','C++ Basics', 'ShreemanYogi','Python cookbook', 'Mechanics'])

    while(True):
        print(".......Welcome to Library.......")
        print("1. Display Books ")
        print("2. Lend Books")
        print("3. Return Book")
        print("4. Add Book")
        choice=int(input("Select an option above==> "))

        if choice==1:
            suraj.DisplayBook()

        elif choice==2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            suraj.LendBook(user, book)

        elif choice==3:
            book=input("Name of book you want to return==>")
            suraj.ReturnBook(book)

        elif choice==4:
            book=input("Name of book you want to add==>")
            suraj.AddBook(book)

        else:
            print("Enter a valid input")

        user_Choice=input("Press q to Quit and c to continue==>")
        if user_Choice=='q':
            break
        else:
            continue

