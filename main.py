import datetime
import os



class LMS:
    """" This class is used to keep record of books library. It has total four module: "Display books", "Issue Books",
    "Return Books", "Add Books", """
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open("List_of_books.txt") as bk:
            content = bk.readlines()

        for lines in content:
            self.books_dict.update({
                str(Id):{
                    "Title":lines.replace("\n",""),
                    "Lender":"",
                    "Status":"Available"

                }

            })
            Id+=1

    def display_books(self):
        print("---------------------List of Books--------------------")
        print("Book ID", "\t", "Title")
        for key, value in self.books_dict.items():
            print(key, '\t\t', value.get("Title"), "- [", value.get("Status"), "]")

    def issue_book(self):
        is_available = False
        user_input = input("Please enter the Book ID:")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d:%M-%S")
        for key, value in self.books_dict.items():
            if user_input == key:
                if self.books_dict[user_input]['Status'] == "Available":
                    print(f"The book {value.get('Title')} is available.")

                    print(f"Issue Date: {current_date}")
                    is_available = True

                else:
                    print("The book is issued to someone else.")


    def add_new_book(self):
        user_book = input("Book Name:")
        user_author = input("Author:")
        new_book_add_in_file = user_book + " by " + user_author
        with open("List_of_books.txt", "a") as bk:
            bk.write(new_book_add_in_file)
        print("The book has been successfully added into the library!")


l = LMS(list_of_books="List_of_books.txt", library_name="Python's library")

def user_choice_lib():
    is_option = True
    while is_option:
        print("1.Display the books are available.\n2.Issue a book\n3.Add a new book.\n4.Quit")
        user_choice = int(input("Please select one of the following:"))
        if user_choice == 1:
            l.display_books()
        elif user_choice == 2:
            l.issue_book()
        elif user_choice==3:
            l.add_new_book()
        else:
            print("Thank you for visiting.")
            is_option = False



print("--------------------------------Welcome To Python Library----------------------------")
user_choice_lib()


