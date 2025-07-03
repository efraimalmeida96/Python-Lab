
from library import Book, User, Library, Paid_User, Free_User, USER_DATABASE

def main():
    
    user_name_check = user_name_access()

    if isinstance(user_name_check, Library):

        while True:

            adm_display()
            while True:
                try:
                    adm_option = int(input('Option: ')) # try/except to user type only number 
                    break
                except ValueError:
                    print('Please type only the numbers on the display')

            if adm_action(adm_option, user_name_check) == False:
                break
            else:
                continue

    else:
        while True:
            
            display_options()
            while True:
                try:
                    user_action = int(input('Option: ')) # try/except to user type only number 
                    break
                except ValueError:
                    print('Please type only the numbers on the display')

            if user_actions(user_action, user_name_check) == False:
                break
            else:
                continue


def display_options():
    
    menu_display = {
        '1': 'Find Book',
        '2': 'Bookshelf',
        '3': 'History',
        '4': 'Return Book',
        '5': 'Exit',
    }
   
    for k, v in menu_display.items():
        print(f'{v:.<30}. [{k}]')

def adm_display():

    menu_display = {
        '1': 'Add Book',
        '2': 'Remove Book',
        '3': 'Exit',
    }

    for k, v in menu_display.items():
        print(f'{v:.<30}. [{k}]')
   

def user_name_access():
    
    while True:

        user_name = input("Enter your username: ").strip()
    
        if user_name in USER_DATABASE:

            if USER_DATABASE[user_name] == 'paid':
                user = Paid_User(user_name)
                print(f"Hello, {user.name}")
                print('Account Premium\n')
                return user
            
            elif USER_DATABASE[user_name] == 'free':
                user = Free_User(user_name)
                print(f"Hello, {user.name}")
                print('Account Free\n')
                return user
            
            elif USER_DATABASE[user_name] == 'adm':
                user = Library()
                print(f"Hello, ADM")
                return user
        
        else:
            print('User not found')


def adm_action(action, user: Library) -> Library:
   
    if action == 1:
        book_title = input('\nBook Title: ').strip().lower()
        author = input('Author Name: ').strip().lower()
        user.add_book(book_title, author)
        print('Book Added')
    
    if action == 2:
        book_title = input('\nBook Title: ').strip().lower()
        author = input('Author Name: ').strip().lower()
        user.remove_book(book_title, author)
        print('Book Removed')

    if action == 3:
        return False


def user_actions(action, user: User) -> User:

    # user.books_borrowed({'book title': 'Spider-Man', 'author': 'Stan Lee'})
    # user.books_borrowed({'book title': 'Spider-Man', 'author': 'Stan Lee'})

    if action == 1:
        book_title = input('\nBook Title: ').strip().lower()
        author = input('Author Name: ').strip().lower()
        print()
        lib_has_book(book_title, author, user)

    if action == 2:
        print(f'\nBookshelf')

        if user.lend_book <= 5 and user.lend_book >= 1:
            print(f'You have borrowed {len(user.bookshelf)} books, still have {5 -len(user.bookshelf)} more')
            for b in user.bookshelf:
                print(b)
            print()

        if user.lend_book <= 1:
            print(f'You borrow your only book')
            print(user.bookshelf)
            print()

    if action == 3:
        print('\nHistory of borrowed books.')
        for b in user.history:
            print(b)
        print()
    
    if action == 4:
        return_book = input('Book to return? ')
        return_book_author = input('Author: ')
        book = Book(return_book, return_book_author)

        for b in user.bookshelf:
            if return_book in b['book title']:
                user.bookshelf.remove(b)
                book.return_book()
                user.lend_book += 1
                print('Book returned\n')

    if action == 5:
        return False
    

def lib_has_book(book_title, author_name, user: User) -> User:

    library = Library()
    book = Book(book_title, author_name)

    found_book = False

    for b in library.book_collection:

        if book.title == b['book title'] and book.author == b['author']:
            found_book = True
            print(f"The book: {b["book title"]} it's in our bookshelf")

            if book.is_available == True:
                print(f"Situation: Available to borrow")

                borrow = input(f'Do you want to borrow: {b['book title']}? [Yes / No] ')
                
                if borrow in 'yYyesYes':

                    if user.lend_book > 0:
                        user.books_borrowed(b)
                        user.history.append(b)
                        book.borrow_book()
                        user.lend_book -= 1
                        print('Book Borrow\n')

                    else:
                        print("You can't borrow more books.\n Return one book to borrow another one.")

                else:
                    print('Book not borrowed')
            
            else:
                print(f"Situation: Unavailable to borrow")

    if found_book == False:
        print('We dont have the book you are looking for.')
            
if __name__ == '__main__':
    main()

