class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Publisher: {self.name}")
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
class Python(Book):
    def __init__(self,name,title,author,price,no_pages):
        super().__init__(name,title,author)
        self.price=price
        self.no_pages=no_pages
    def display_python_book_info(self):
        super().display()
        print(f"Price: {self.price}")
        print(f"No of pages:{self.no_pages}")
python_book = Python('Reilly media','Python learning','Mark Lutz',139,579)
python_book.display_python_book_info()
