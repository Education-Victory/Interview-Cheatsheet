import streamlit as st

def ds_java_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('ArrayList')
        col1.code('''
    // Example: Initializing the ArrayList
    ArrayList<String> books = new ArrayList<>();

    // Example: Adding a new book to the list
    books.add("The Great Gatsby");

    // Example: Retrieving the name of the first book
    String firstBook = books.get(0); // returns "The Great Gatsby"

    // Example: Removing a book that was sold
    books.remove("The Great Gatsby");

    // Example: Clearing the book list at the end of the season
    books.clear();

    // Example: Checking if a book is in stock
    boolean isInStock = books.contains("1984"); // returns true or false

    // Example: Checking if the book list is empty before restocking
    boolean isBookListEmpty = books.isEmpty(); // returns true or false

    // Example: Finding the index of a book
    int indexOf1984 = books.indexOf("1984"); // returns the index of "1984"

    // Example: Converting the book list to an array
    String[] bookArray = books.toArray(new String[0]); // converts to an array
        ''', language="java")

        col1.subheader('LinkedList')
        col1.code('''
    // Example: Initializing the LinkedList
    LinkedList<String> books = new LinkedList<>();

    // Example: Adding a new book to the list
    books.add("The Great Gatsby");

    // Example: Retrieving the name of the first book
    String firstBook = books.get(0); // returns "The Great Gatsby"

    // Example: Removing a book that was sold
    books.remove("The Great Gatsby");

    // Example: Checking how many books are currently available
    int numberOfBooks = books.size(); // returns the current count

    // Example: Clearing the book list
    books.clear();

    // Example: Checking if a book is in stock
    boolean isInStock = books.contains("1984"); // returns true or false

    // Example: Checking if the list is empty
    boolean isListEmpty = books.isEmpty(); // returns true or false

    // Example: Adding a book to the front of the list
    books.addFirst("Moby Dick"); // adds "Moby Dick" at the beginning

    // Example: Adding a book to the end of the list
    books.addLast("To Kill a Mockingbird"); // adds "To Kill a Mockingbird" at the end

    // Example: Removing the first book from the list
    String firstBookRemoved = books.removeFirst(); // removes and returns the first book
        ''', language="java")

        col1.subheader('Stack')
        col1.code('''
    // Example: Initializing the Stack
    Stack<String> books = new Stack<>();

    // Example: Adding a book to the stack
    books.push("Harry Potter");

    // Example: Removing the top book from the stack
    String topBook = books.pop(); // removes and returns "Harry Potter"

    // Example: Viewing the top book without removing it
    String topBookView = books.peek(); // returns "Harry Potter" without removing

    // Example: Checking if the stack is empty
    boolean isStackEmpty = books.isEmpty(); // returns true or false

    // Example: Checking how many books are in the stack
    int numberOfBooks = books.size(); // returns the current count

    // Example: Clearing the stack
    books.clear(); // removes all books from the stack

    // Example: Checking if a specific book is in the stack
    boolean hasBook = books.contains("The Hobbit"); // returns true or false

    // Example: Converting the stack to an array
    String[] bookArray = books.toArray(new String[0]); // converts to an array

    // Example: Iterating through the stack
    Iterator<String> it = books.iterator(); // creates an iterator for the stack
        ''', language="java")

        col1.subheader('HashMap')
        col1.code('''
    // Example: Initializing the HashMap
    HashMap<String, String> books = new HashMap<>();

    // Example: Adding a book with its author to the HashMap
    books.put("The Great Gatsby", "F. Scott Fitzgerald");

    // Example: Retrieving the author of a specific book
    String author = books.get("The Great Gatsby"); // returns "F. Scott Fitzgerald"

    // Example: Removing a book from the HashMap
    books.remove("The Great Gatsby"); // removes the entry for "The Great Gatsby"

    // Example: Checking if a book is in the HashMap
    boolean hasBook = books.containsKey("1984"); // returns true or false

    // Example: Checking if a specific author is in the HashMap
    boolean hasAuthor = books.containsValue("George Orwell"); // returns true or false

    // Example: Checking if the HashMap is empty
    boolean isMapEmpty = books.isEmpty(); // returns true or false

    // Example: Checking how many books are in the HashMap
    int numberOfBooks = books.size(); // returns the current count

    // Example: Clearing the HashMap
    books.clear(); // removes all entries from the HashMap

    // Example: Retrieving a set of all book titles
    Set<String> bookTitles = books.keySet(); // returns a set of keys

    // Example: Retrieving a collection of all authors
    Collection<String> authors = books.values(); // returns a collection of values
        ''', language="java")

    with col2:

        col2.subheader('PriorityQueue')
        col2.code('''
    // Example: Initializing the PriorityQueue
    PriorityQueue<String> books = new PriorityQueue<>();

    // Example: Adding a book to the priority queue
    books.add("The Great Gatsby");

    // Example: Offering a book to the priority queue
    books.offer("1984"); // adds "1984" to the queue

    // Example: Removing and returning the highest priority book
    String topBook = books.poll(); // removes and returns the highest priority book

    // Example: Viewing the highest priority book without removing it
    String topBookView = books.peek(); // returns the highest priority book without removing

    // Example: Checking if the priority queue is empty
    boolean isQueueEmpty = books.isEmpty(); // returns true or false

    // Example: Checking how many books are in the priority queue
    int numberOfBooks = books.size(); // returns the current count

    // Example: Removing a specific book from the queue
    books.remove("The Great Gatsby"); // removes "The Great Gatsby"

    // Example: Checking if a specific book is in the queue
    boolean hasBook = books.contains("1984"); // returns true or false

    // Example: Converting the priority queue to an array
    String[] bookArray = books.toArray(new String[0]); // converts to an array

    // Example: Iterating through the priority queue
    Iterator<String> it = books.iterator(); // creates an iterator for the queue
        ''', language="java")

        col2.subheader('Queue')
        col2.code('''
    // Example: Initializing the Queue
    Queue<String> books = new LinkedList<>();

    // Example: Adding a new book to the queue
    books.add("The Great Gatsby");

    // Example: Offering a book to the queue
    books.offer("1984"); // adds "1984" to the queue

    // Example: Removing and returning the head of the queue
    String firstBook = books.poll(); // removes and returns the first book

    // Example: Viewing the head of the queue without removing it
    String firstBookView = books.peek(); // returns the first book without removing

    // Example: Checking if the queue is empty
    boolean isQueueEmpty = books.isEmpty(); // returns true or false

    // Example: Checking how many books are in the queue
    int numberOfBooks = books.size(); // returns the current count

    // Example: Removing the head of the queue
    String firstBookRemoved = books.remove(); // removes and returns the head of the queue

    // Example: Checking if a specific book is in the queue
    boolean hasBook = books.contains("1984"); // returns true or false

    // Example: Converting the queue to an array
    String[] bookArray = books.toArray(new String[0]); // converts to an array

    // Example: Iterating through the queue
    Iterator<String> it = books.iterator(); // creates an iterator for the queue
        ''', language="java")

        col2.subheader('HashSet')
        col2.code('''
    // Example: Initializing the HashSet
    HashSet<String> books = new HashSet<>();

    // Example: Adding a new book to the HashSet
    books.add("The Great Gatsby");

    // Example: Removing a book from the HashSet
    books.remove("The Great Gatsby"); // removes "The Great Gatsby"

    // Example: Checking if a specific book is in the HashSet
    boolean hasBook = books.contains("1984"); // returns true or false

    // Example: Checking if the HashSet is empty
    boolean isSetEmpty = books.isEmpty(); // returns true or false

    // Example: Checking how many books are in the HashSet
    int numberOfBooks = books.size(); // returns the current count

    // Example: Clearing the HashSet
    books.clear(); // removes all books from the HashSet

    // Example: Converting the HashSet to an array
    String[] bookArray = books.toArray(new String[0]); // converts to an array

    // Example: Iterating through the HashSet
    Iterator<String> it = books.iterator(); // creates an iterator for the HashSet

    // Example: Removing multiple books from the HashSet
    books.removeAll(Arrays.asList("1984", "Moby Dick")); // removes specified books

    // Example: Retaining only specified books in the HashSet
    books.retainAll(Arrays.asList("The Great Gatsby")); // keeps only "The Great Gatsby"
        ''', language="java")

        col2.subheader('TreeMap')
        col2.code('''
    // Example: Initializing the TreeMap
    TreeMap<String, String> books = new TreeMap<>();

    // Example: Adding a book with its author to the TreeMap
    books.put("The Great Gatsby", "F. Scott Fitzgerald");

    // Example: Retrieving the author of a specific book
    String author = books.get("The Great Gatsby"); // returns "F. Scott Fitzgerald"

    // Example: Removing a book from the TreeMap
    books.remove("The Great Gatsby"); // removes the entry for "The Great Gatsby"

    // Example: Retrieving the first book in the TreeMap
    String firstBook = books.firstKey(); // returns the first key

    // Example: Retrieving the last book in the TreeMap
    String lastBook = books.lastKey(); // returns the last key

    // Example: Checking if a book is in the TreeMap
    boolean hasBook = books.containsKey("1984"); // returns true or false

    // Example: Checking if the TreeMap is empty
    boolean isMapEmpty = books.isEmpty(); // returns true or false

    // Example: Checking how many books are in the TreeMap
    int numberOfBooks = books.size(); // returns the current count

    // Example: Clearing the TreeMap
    books.clear(); // removes all entries from the TreeMap

    // Example: Retrieving a set of all book titles
    Set<String> bookTitles = books.keySet(); // returns a set of keys
        ''', language="java")
