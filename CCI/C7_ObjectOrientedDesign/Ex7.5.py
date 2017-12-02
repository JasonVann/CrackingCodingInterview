import copy

class User():
    id = 0
    def __init__(self, user_name):
        User.id += 1
        self.id = type(self).id
        self.name = user_name
        self.books = []
        self.last_read = None

class Book():
    def __init__(self, name):
        self.name = name
        self.read_page = 0

class OnlineReader():
    def __init__(self):
        self.books = []
        self.users = set()

    def log_in(self, user):
        if user in self.users:
            return True
        return False

    def create_user(self, user_name):
        user = User(user_name)
        self.users.add(user)

    def buy_book(self, user_name, book_name):
        book = Book(book_name)
        self.user.books.append(book)

    def pick_book(self, user, book_name):
        if book_name is None:
            return user.last_read
        else:
            for book in self.books:
                if book.name == book_name:
                    return book

    def read(self, user, book):
        # read
        book.read_page += 1
