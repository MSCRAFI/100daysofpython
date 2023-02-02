class Library:
    def __init__(self):
        self.book_name = []  # list for books
        self.count = 0

    def addbooks(self):
        while True:
            get_books = input("Enter your book or type exit to close the \
program:\n>> ")
            if get_books == "exit":
                break
            self.count += 1
            lib.book_name.append(get_books)
            self.no_books = len(lib.book_name)  # for no of books
            print(f"You have total of {self.no_books} books. Below is all \
your books:")
            for i in self.book_name:
                print(i)


lib = Library()
lib.addbooks()
