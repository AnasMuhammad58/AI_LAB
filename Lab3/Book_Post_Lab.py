class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return f'You have borrowed "{self.title}" by {self.author}.'
        else:
            return f'"{self.title}" by {self.author} is currently unavailable.'

    def return_book(self):
        if not self.available:
            self.available = True
            return f'You have returned "{self.title}" by {self.author}.'
        else:
            return f'"{self.title}" by {self.author} was not borrowed.'

# Example usage:
book1 = Book('Total Recall', 'Arnold Schwarzenegger')
print(book1.borrow())
print(book1.borrow())
print(book1.return_book())
print(book1.return_book())
