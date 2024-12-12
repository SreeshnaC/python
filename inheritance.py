class Publisher:
    def __init__(self,publisher_name):
        self.publisher_name=publisher_name
    def display_publisher(self):
        print("Publisher:{self.publisher_name}")

class Book(Publisher):
    def __init__(self,publisher_name,title,author):
        super().__init__(publisher_name)
        self.title=title
        self.author=author
    def display_Book(self):
