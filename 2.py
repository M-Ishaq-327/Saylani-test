#TASK NUM 2:
class Book():
    def __init__(self,title,author,isbn,is_borrowed):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed=is_borrowed

    def borrow(self):
        is_borrowed=True
    def return_book(self):
        is_borrowed=False
    
class DigitalBook(Book):
    def __init__(self,title,author,isbn,is_borrowed,file_format):
        super().__init__(title,author,isbn,is_borrowed)
        self.file_format=file_format

    def borrow(self):
        super().__init__()
        print(f'yes book can be borrow online also from {self.file_format}')

class AudioBook(Book):
    def __init__(self,title,author,isbn,is_borrowed,duration):
        super().__init__(title,author,isbn,is_borrowed)
        self.duration=duration

    def borrow(self):
        super().__init__()
        print(f'Yes book is available for streaming for time duration of {self.duration} hrs ')



class User():
    def __init__(self,user_id,name,borrowed_books):
        self.user_id=user_id
        self.name=name
        self.borrowed_book=borrowed_books

    def borrow_book(self):
        for book in borrowed_book:
            if book not in borrowed_book:
                borrowed_book.append(book)
            else:
                pass

    def return_book(self):
        for book in borrowed_book:
            if book in borrowed_book:
                borrowed_book.remove(book)



class Library():
    def __init__(self,name,book,user):
        self.name=name
        self.book=book
        self.user=user

