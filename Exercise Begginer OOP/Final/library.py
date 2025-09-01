
USER_DATABASE = {
    'adm': 'adm',
    'user1': 'free',
    'user2': 'paid',
}

class User:

    def __init__(self, username):
        self.name = username
        self.history = []
        self.bookshelf = []
        self.lend_book = 0

    def books_borrowed(self, book):

        if len(self.bookshelf) < self.lend_book:
            self.bookshelf.append(book)


    # def see_history(self):

    #     if not self.history:
    #         pass
    #     else:

    def __str__(self):
        return f'{self.name}'

        
class Paid_User(User):

    def __init__(self, username):
        super().__init__(username)
        self.lend_book = 5

class Free_User(User):

    def __init__(self, username):
        super().__init__(username)
        self.lend_book = 1


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._available = True
    
    @property
    def is_available(self):
        return self._available
    
    def borrow_book(self):
        if self._available:
            self._available = False
            return self._available

    def return_book(self):
        if self._available == False:
            self._available = True
        return self._available


class Library:

    def __init__(self):
        self.book_collection = [
            {'book title': 'narnia', 'author': 'cslewis'},
            {'book title': 'spider-man', 'author': 'stan lee'},
            {'book title': 'lord of ther ings', 'author': 'tolkien'},
            {'book title': 'don quixote', 'author': 'miguel de servantes'},
            {'book title': 'a paciente silenciosa', 'author': 'alex michaelises'},
            ]

    def add_book(self, title, author):
        self.book_collection.append({'book title': title,'author': author,})

    def remove_book(self, title, author):
        self.book_collection.remove({'book title': title,'author': author,})

    # create a method to edit if adm type wrong 
    # create a conditional if adm type wrong