import streamlit as st

def ds_python_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('ArrayList')
        col1.code('''
    # Example: Initializing the list
    books = []

    # Example: Adding a new book to the list
    books.append("The Great Gatsby")

    # Example: Retrieving the name of the first book
    first_book = books[0]  # returns "The Great Gatsby"

    # Example: Removing a book that was sold
    books.remove("The Great Gatsby")

    # Example: Clearing the book list at the end of the season
    books.clear()

    # Example: Checking if a book is in stock
    is_in_stock = "1984" in books  # returns True or False

    # Example: Checking if the book list is empty before restocking
    is_book_list_empty = len(books) == 0  # returns True or False

    # Example: Finding the index of a book
    index_of_1984 = books.index("1984") if "1984" in books else -1  # returns the index of "1984" or -1

    # Example: Converting the book list to an array
    book_array = list(books)  # converts to a list
        ''', language="python")

        col1.subheader('LinkedList')
        col1.code('''
    # Example: Initializing the deque
    from collections import deque
    books = deque()

    # Example: Adding a new book to the list
    books.append("The Great Gatsby")

    # Example: Retrieving the name of the first book
    first_book = books[0]  # returns "The Great Gatsby"

    # Example: Removing a book that was sold
    books.remove("The Great Gatsby")

    # Example: Checking how many books are currently available
    number_of_books = len(books)  # returns the current count

    # Example: Clearing the book list
    books.clear()

    # Example: Checking if a book is in stock
    is_in_stock = "1984" in books  # returns True or False

    # Example: Checking if the list is empty
    is_list_empty = len(books) == 0  # returns True or False

    # Example: Adding a book to the front of the list
    books.appendleft("Moby Dick")  # adds "Moby Dick" at the beginning

    # Example: Adding a book to the end of the list
    books.append("To Kill a Mockingbird")  # adds "To Kill a Mockingbird" at the end

    # Example: Removing the first book from the list
    first_book_removed = books.popleft()  # removes and returns the first book
        ''', language="python")

        col1.subheader('Stack')
        col1.code('''
    # Example: Initializing the stack
    books = []

    # Example: Adding a book to the stack
    books.append("Harry Potter")

    # Example: Removing the top book from the stack
    top_book = books.pop()  # removes and returns "Harry Potter"

    # Example: Viewing the top book without removing it
    top_book_view = books[-1] if books else None  # returns "Harry Potter" without removing

    # Example: Checking if the stack is empty
    is_stack_empty = len(books) == 0  # returns True or False

    # Example: Checking how many books are in the stack
    number_of_books = len(books)  # returns the current count

    # Example: Clearing the stack
    books.clear()  # removes all books from the stack

    # Example: Checking if a specific book is in the stack
    has_book = "The Hobbit" in books  # returns True or False

    # Example: Converting the stack to an array
    book_array = list(books)  # converts to a list

    # Example: Iterating through the stack
    for book in books:  # creates an iterator for the stack
        print(book)
        ''', language="python")

        col1.subheader('HashMap')
        col1.code('''
    # Example: Initializing the dictionary
    books = {}

    # Example: Adding a book with its author to the dictionary
    books["The Great Gatsby"] = "F. Scott Fitzgerald"

    # Example: Retrieving the author of a specific book
    author = books.get("The Great Gatsby")  # returns "F. Scott Fitzgerald"

    # Example: Removing a book from the dictionary
    books.pop("The Great Gatsby", None)  # removes the entry for "The Great Gatsby"

    # Example: Checking if a book is in the dictionary
    has_book = "1984" in books  # returns True or False

    # Example: Checking if a specific author is in the dictionary
    has_author = "George Orwell" in books.values()  # returns True or False

    # Example: Checking if the dictionary is empty
    is_map_empty = len(books) == 0  # returns True or False

    # Example: Checking how many books are in the dictionary
    number_of_books = len(books)  # returns the current count

    # Example: Clearing the dictionary
    books.clear()  # removes all entries from the dictionary

    # Example: Retrieving a set of all book titles
    book_titles = set(books.keys())  # returns a set of keys

    # Example: Retrieving a collection of all authors
    authors = list(books.values())  # returns a list of values
        ''', language="python")

    with col2:

        col2.subheader('PriorityQueue')
        col2.code('''
    # Example: Initializing the priority queue
    import heapq
    books = []

    # Example: Adding a book to the priority queue
    heapq.heappush(books, "The Great Gatsby")

    # Example: Offering a book to the priority queue
    heapq.heappush(books, "1984")  # adds "1984" to the queue

    # Example: Removing and returning the highest priority book
    top_book = heapq.heappop(books)  # removes and returns the highest priority book

    # Example: Viewing the highest priority book without removing it
    top_book_view = books[0] if books else None  # returns the highest priority book without removing

    # Example: Checking if the priority queue is empty
    is_queue_empty = len(books) == 0  # returns True or False

    # Example: Checking how many books are in the priority queue
    number_of_books = len(books)  # returns the current count

    # Example: Removing a specific book from the queue
    books.remove("The Great Gatsby")  # removes "The Great Gatsby"

    # Example: Checking if a specific book is in the queue
    has_book = "1984" in books  # returns True or False

    # Example: Converting the priority queue to an array
    book_array = list(books)  # converts to a list

    # Example: Iterating through the priority queue
    for book in books:  # creates an iterator for the queue
        print(book)
        ''', language="python")

        col2.subheader('Queue')
        col2.code('''
    # Example: Initializing the queue
    from collections import deque
    books = deque()

    # Example: Adding a new book to the queue
    books.append("The Great Gatsby")

    # Example: Offering a book to the queue
    books.append("1984")  # adds "1984" to the queue

    # Example: Removing and returning the head of the queue
    first_book = books.popleft()  # removes and returns the first book

    # Example: Viewing the head of the queue without removing it
    first_book_view = books[0] if books else None  # returns the first book without removing

    # Example: Checking if the queue is empty
    is_queue_empty = len(books) == 0  # returns True or False

    # Example: Checking how many books are in the queue
    number_of_books = len(books)  # returns the current count

    # Example: Removing the head of the queue
    first_book_removed = books.popleft()  # removes and returns the head of the queue

    # Example: Checking if a specific book is in the queue
    has_book = "1984" in books  # returns True or False

    # Example: Converting the queue to an array
    book_array = list(books)  # converts to a list

    # Example: Iterating through the queue
    for book in books:  # creates an iterator for the queue
        print(book)
        ''', language="python")

        col2.subheader('HashSet')
        col2.code('''
    # Example: Initializing the set
    books = set()

    # Example: Adding a new book to the set
    books.add("The Great Gatsby")

    # Example: Removing a book from the set
    books.discard("The Great Gatsby")  # removes "The Great Gatsby"

    # Example: Checking if a specific book is in the set
    has_book = "1984" in books  # returns True or False

    # Example: Checking if the set is empty
    is_set_empty = len(books) == 0  # returns True or False

    # Example: Checking how many books are in the set
    number_of_books = len(books)  # returns the current count

    # Example: Clearing the set
    books.clear()  # removes all books from the set

    # Example: Converting the set to an array
    book_array = list(books)  # converts to a list

    # Example: Iterating through the set
    for book in books:  # creates an iterator for the set
        print(book)

    # Example: Removing multiple books from the set
    books.difference_update({"1984", "Moby Dick"})  # removes specified books

    # Example: Retaining only specified books in the set
    books.intersection_update({"The Great Gatsby"})  # keeps only "The Great Gatsby"
        ''', language="python")

        col2.subheader('TreeMap')
        col2.code('''
    # Example: Initializing the SortedDict
    from sortedcontainers import SortedDict
    books = SortedDict()

    # Example: Adding a book with its author to the SortedDict
    books['The Great Gatsby'] = 'F. Scott Fitzgerald'

    # Example: Retrieving the author of a specific book
    author = books.get('The Great Gatsby')  # returns 'F. Scott Fitzgerald'

    # Example: Removing a book from the SortedDict
    books.pop('The Great Gatsby', None)  # removes the entry for 'The Great Gatsby'

    # Example: Retrieving the first book in the SortedDict
    first_book = books.peekitem(0)[0] if len(books) > 0 else None  # returns the first key

    # Example: Retrieving the last book in the SortedDict
    last_book = books.peekitem(-1)[0] if len(books) > 0 else None  # returns the last key

    # Example: Checking if a book is in the SortedDict
    has_book = '1984' in books  # returns True or False

    # Example: Checking if the SortedDict is empty
    is_map_empty = len(books) == 0  # returns True or False

    # Example: Checking how many books are in the SortedDict
    number_of_books = len(books)  # returns the current count

    # Example: Clearing the SortedDict
    books.clear()  # removes all entries from the SortedDict

    # Example: Retrieving a set of all book titles
    book_titles = set(books.keys())  # returns a set of keys
    ''', language="python")
