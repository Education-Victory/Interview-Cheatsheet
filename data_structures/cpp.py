import streamlit as st

def ds_cpp_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('ArrayList')
        col1.code('''
    // Example: Initializing the vector
    std::vector<std::string> books;

    // Example: Adding a new book to the list
    books.push_back("The Great Gatsby");

    // Example: Retrieving the name of the first book
    std::string first_book = books[0]; // returns "The Great Gatsby"

    // Example: Removing a book that was sold
    books.erase(std::remove(books.begin(), books.end(), "The Great Gatsby"), books.end());

    // Example: Clearing the book list at the end of the season
    books.clear();

    // Example: Checking if a book is in stock
    bool is_in_stock = std::find(books.begin(), books.end(), "1984") != books.end(); // returns true or false

    // Example: Checking if the book list is empty before restocking
    bool is_book_list_empty = books.empty(); // returns true or false

    // Example: Finding the index of a book
    auto it = std::find(books.begin(), books.end(), "1984");
    int index_of_1984 = (it != books.end()) ? std::distance(books.begin(), it) : -1; // returns the index or -1

    // Example: Converting the book list to an array
    std::vector<std::string> book_array = books; // copies to a vector
        ''', language="cpp")

        col1.subheader('LinkedList')
        col1.code('''
    // Example: Initializing the list
    std::list<std::string> books;

    // Example: Adding a new book to the list
    books.push_back("The Great Gatsby");

    // Example: Retrieving the name of the first book
    std::string first_book = books.front(); // returns "The Great Gatsby"

    // Example: Removing a book that was sold
    books.remove("The Great Gatsby");

    // Example: Checking how many books are currently available
    int number_of_books = books.size(); // returns the current count

    // Example: Clearing the book list
    books.clear();

    // Example: Checking if a book is in stock
    bool is_in_stock = std::find(books.begin(), books.end(), "1984") != books.end(); // returns true or false

    // Example: Checking if the list is empty
    bool is_list_empty = books.empty(); // returns true or false

    // Example: Adding a book to the front of the list
    books.push_front("Moby Dick"); // adds "Moby Dick" at the beginning

    // Example: Adding a book to the end of the list
    books.push_back("To Kill a Mockingbird"); // adds "To Kill a Mockingbird" at the end

    // Example: Removing the first book from the list
    books.pop_front(); // removes the first book
        ''', language="cpp")

        col1.subheader('Stack')
        col1.code('''
    // Example: Initializing the stack
    std::stack<std::string> books;

    // Example: Adding a book to the stack
    books.push("Harry Potter");

    // Example: Removing the top book from the stack
    std::string top_book = books.top(); // returns "Harry Potter"
    books.pop(); // removes the top book

    // Example: Viewing the top book without removing it
    std::string top_book_view = books.top(); // returns "Harry Potter" without removing

    // Example: Checking if the stack is empty
    bool is_stack_empty = books.empty(); // returns true or false

    // Example: Checking how many books are in the stack
    int number_of_books = books.size(); // returns the current count

    // Example: Clearing the stack
    while (!books.empty()) books.pop(); // removes all books from the stack

    // Example: Checking if a specific book is in the stack
    // Note: Stack does not support direct search; requires additional data structure

    // Example: Converting the stack to an array (vector)
    std::vector<std::string> book_array;
    while (!books.empty()) {
        book_array.push_back(books.top());
        books.pop();
    }

    // Example: Iterating through the stack
    for (const auto& book : book_array) { // creates an iterator for the vector
        std::cout << book << std::endl;
    }
        ''', language="cpp")

        col1.subheader('HashMap')
        col1.code('''
    // Example: Initializing the unordered_map
    std::unordered_map<std::string, std::string> books;

    // Example: Adding a book with its author to the map
    books["The Great Gatsby"] = "F. Scott Fitzgerald";

    // Example: Retrieving the author of a specific book
    std::string author = books.at("The Great Gatsby"); // returns "F. Scott Fitzgerald"

    // Example: Removing a book from the map
    books.erase("The Great Gatsby"); // removes the entry for "The Great Gatsby"

    // Example: Checking if a book is in the map
    bool has_book = books.find("1984") != books.end(); // returns true or false

    // Example: Checking if a specific author is in the map
    bool has_author = std::any_of(books.begin(), books.end(), [](const auto& pair) { return pair.second == "George Orwell"; }); // returns true or false

    // Example: Checking if the map is empty
    bool is_map_empty = books.empty(); // returns true or false

    // Example: Checking how many books are in the map
    int number_of_books = books.size(); // returns the current count

    // Example: Clearing the map
    books.clear(); // removes all entries from the map

    // Example: Retrieving a set of all book titles
    std::set<std::string> book_titles;
    for (const auto& pair : books) {
        book_titles.insert(pair.first);
    }

    // Example: Retrieving a collection of all authors
    std::vector<std::string> authors;
    for (const auto& pair : books) {
        authors.push_back(pair.second);
    }
        ''', language="cpp")

    with col2:

        col2.subheader('PriorityQueue')
        col2.code('''
    // Example: Initializing the priority queue
    std::priority_queue<std::string> books;

    // Example: Adding a book to the priority queue
    books.push("The Great Gatsby");

    // Example: Offering a book to the priority queue
    books.push("1984"); // adds "1984" to the queue

    // Example: Removing and returning the highest priority book
    std::string top_book = books.top(); // returns the highest priority book
    books.pop(); // removes the highest priority book

    // Example: Viewing the highest priority book without removing it
    std::string top_book_view = books.top(); // returns the highest priority book without removing

    // Example: Checking if the priority queue is empty
    bool is_queue_empty = books.empty(); // returns true or false

    // Example: Checking how many books are in the priority queue
    int number_of_books = books.size(); // returns the current count

    // Example: Removing a specific book from the queue
    // Note: Priority queue does not support direct removal; requires rebuilding

    // Example: Checking if a specific book is in the queue
    // Note: Priority queue does not support direct search; requires additional data structure

    // Example: Converting the priority queue to an array (vector)
    std::vector<std::string> book_array;
    while (!books.empty()) {
        book_array.push_back(books.top());
        books.pop();
    }

    // Example: Iterating through the priority queue
    for (const auto& book : book_array) { // creates an iterator for the vector
        std::cout << book << std::endl;
    }
        ''', language="cpp")

        col2.subheader('Queue')
        col2.code('''
    // Example: Initializing the queue
    std::queue<std::string> books;

    // Example: Adding a new book to the queue
    books.push("The Great Gatsby");

    // Example: Offering a book to the queue
    books.push("1984"); // adds "1984" to the queue

    // Example: Removing and returning the head of the queue
    std::string first_book = books.front(); // returns the first book
    books.pop(); // removes the head of the queue

    // Example: Viewing the head of the queue without removing it
    std::string first_book_view = books.front(); // returns the first book without removing

    // Example: Checking if the queue is empty
    bool is_queue_empty = books.empty(); // returns true or false

    // Example: Checking how many books are in the queue
    int number_of_books = books.size(); // returns the current count

    // Example: Removing the head of the queue
    first_book = books.front(); // retrieves the head of the queue
    books.pop(); // removes the head of the queue

    // Example: Checking if a specific book is in the queue
    // Note: Queue does not support direct search; requires additional data structure

    // Example: Converting the queue to an array (vector)
    std::vector<std::string> book_array;
    while (!books.empty()) {
        book_array.push_back(books.front());
        books.pop();
    }

    // Example: Iterating through the queue
    for (const auto& book : book_array) { // creates an iterator for the vector
        std::cout << book << std::endl;
    }
        ''', language="cpp")

        col2.subheader('HashSet')
        col2.code('''
    // Example: Initializing the unordered_set
    std::unordered_set<std::string> books;

    // Example: Adding a new book to the set
    books.insert("The Great Gatsby");

    // Example: Removing a book from the set
    books.erase("The Great Gatsby"); // removes "The Great Gatsby"

    // Example: Checking if a specific book is in the set
    bool has_book = books.find("1984") != books.end(); // returns true or false

    // Example: Checking if the set is empty
    bool is_set_empty = books.empty(); // returns true or false

    // Example: Checking how many books are in the set
    int number_of_books = books.size(); // returns the current count

    // Example: Clearing the set
    books.clear(); // removes all books from the set

    // Example: Converting the set to an array (vector)
    std::vector<std::string> book_array(books.begin(), books.end()); // converts to a vector

    // Example: Iterating through the set
    for (const auto& book : books) { // creates an iterator for the set
        std::cout << book << std::endl;
    }

    // Example: Removing multiple books from the set
    books.erase("1984"); // removes specified books

    // Example: Retaining only specified books in the set
    std::unordered_set<std::string> to_keep = {"The Great Gatsby"};
    for (auto it = books.begin(); it != books.end();) {
        if (to_keep.find(*it) == to_keep.end()) {
            it = books.erase(it); // keeps only "The Great Gatsby"
        } else {
            ++it;
        }
    }
        ''', language="cpp")

        col2.subheader('TreeMap')
        col2.code('''
    // Example: Initializing the map
    std::map<std::string, std::string> books;

    // Example: Adding a book with its author to the map
    books["The Great Gatsby"] = "F. Scott Fitzgerald";

    // Example: Retrieving the author of a specific book
    std::string author = books.at("The Great Gatsby"); // returns "F. Scott Fitzgerald"

    // Example: Removing a book from the map
    books.erase("The Great Gatsby"); // removes the entry for "The Great Gatsby"

    // Example: Retrieving the first book in the map
    std::string first_book = books.begin()->first; // returns the first key

    // Example: Retrieving the last book in the map
    std::string last_book = (--books.end())->first; // returns the last key

    // Example: Checking if a book is in the map
    bool has_book = books.find("1984") != books.end(); // returns true or false

    // Example: Checking if the map is empty
    bool is_map_empty = books.empty(); // returns true or false

    // Example: Checking how many books are in the map
    int number_of_books = books.size(); // returns the current count

    // Example: Clearing the map
    books.clear(); // removes all entries from the map

    // Example: Retrieving a set of all book titles
    std::set<std::string> book_titles;
    for (const auto& pair : books) {
        book_titles.insert(pair.first);
    }
        ''', language="cpp")

