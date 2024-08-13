import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    col1.subheader('ArrayList')
    col1.code('''
add(E e) // Example: Adding a new book to the list
ArrayList<String> books = new ArrayList<>();
books.add("The Great Gatsby");

get(int index) // Example: Retrieving the name of the first book
String firstBook = books.get(0); // returns "The Great Gatsby"

remove(Object o) // Example: Removing a book that was sold
books.remove("The Great Gatsby");

clear() // Example: Clearing the book list at the end of the season
books.clear();

contains(Object o) // Example: Checking if a book is in stock
boolean isInStock = books.contains("1984"); // returns true or false

isEmpty() // Example: Checking if the book list is empty before restocking
boolean isBookListEmpty = books.isEmpty(); // returns true or false

indexOf(Object o) // Example: Finding the index of a book
int indexOf1984 = books.indexOf("1984"); // returns the index of "1984"

toArray() // Example: Converting the book list to an array
String[] bookArray = books.toArray(new String[0]); // converts to an array
    ''', language="java")

    col1.subheader('LinkedList')
    col1.code('''
add(E e) // Example: Adding a new book to the list
LinkedList<String> books = new LinkedList<>();
books.add("The Great Gatsby");

get(int index) // Example: Retrieving the name of the first book
String firstBook = books.get(0); // returns "The Great Gatsby"

remove(Object o) // Example: Removing a book that was sold
books.remove("The Great Gatsby");

size() // Example: Checking how many books are currently available
int numberOfBooks = books.size(); // returns the current count

clear() // Example: Clearing the book list
books.clear();

contains(Object o) // Example: Checking if a book is in stock
boolean isInStock = books.contains("1984"); // returns true or false

isEmpty() // Example: Checking if the list is empty
boolean isListEmpty = books.isEmpty(); // returns true or false

addFirst(E e) // Example: Adding a book to the front of the list
books.addFirst("Moby Dick"); // adds "Moby Dick" at the beginning

addLast(E e) // Example: Adding a book to the end of the list
books.addLast("To Kill a Mockingbird"); // adds "To Kill a Mockingbird" at the end

removeFirst() // Example: Removing the first book from the list
String firstBookRemoved = books.removeFirst(); // removes and returns the first book
    ''', language="java")

    col1.subheader('Stack')
    col1.code('''
push(E item) // Example: Adding a book to the stack
Stack<String> books = new Stack<>();
books.push("Harry Potter");

pop() // Example: Removing the top book from the stack
String topBook = books.pop(); // removes and returns "Harry Potter"

peek() // Example: Viewing the top book without removing it
String topBookView = books.peek(); // returns "Harry Potter" without removing

isEmpty() // Example: Checking if the stack is empty
boolean isStackEmpty = books.isEmpty(); // returns true or false

size() // Example: Checking how many books are in the stack
int numberOfBooks = books.size(); // returns the current count

clear() // Example: Clearing the stack
books.clear(); // removes all books from the stack

contains(Object o) // Example: Checking if a specific book is in the stack
boolean hasBook = books.contains("The Hobbit"); // returns true or false

toArray() // Example: Converting the stack to an array
String[] bookArray = books.toArray(new String[0]); // converts to an array

iterator() // Example: Iterating through the stack
Iterator<String> it = books.iterator(); // creates an iterator for the stack
    ''', language="java")


with col2:

    col2.subheader('PriorityQueue')
    col2.code('''
add(E e) // Example: Adding a book to the priority queue
PriorityQueue<String> books = new PriorityQueue<>();
books.add("The Great Gatsby");

offer(E e) // Example: Offering a book to the priority queue
books.offer("1984"); // adds "1984" to the queue

poll() // Example: Removing and returning the highest priority book
String topBook = books.poll(); // removes and returns the highest priority book

peek() // Example: Viewing the highest priority book without removing it
String topBookView = books.peek(); // returns the highest priority book without removing

isEmpty() // Example: Checking if the priority queue is empty
boolean isQueueEmpty = books.isEmpty(); // returns true or false

size() // Example: Checking how many books are in the priority queue
int numberOfBooks = books.size(); // returns the current count

remove(Object o) // Example: Removing a specific book from the queue
books.remove("The Great Gatsby"); // removes "The Great Gatsby"

contains(Object o) // Example: Checking if a specific book is in the queue
boolean hasBook = books.contains("1984"); // returns true or false

toArray() // Example: Converting the priority queue to an array
String[] bookArray = books.toArray(new String[0]); // converts to an array

iterator() // Example: Iterating through the priority queue
Iterator<String> it = books.iterator(); // creates an iterator for the queue
    ''', language="java")

    col2.subheader('Queue')
    col2.code('''
add(E e) // Example: Adding a new book to the queue
Queue<String> books = new LinkedList<>();
books.add("The Great Gatsby");

offer(E e) // Example: Offering a book to the queue
books.offer("1984"); // adds "1984" to the queue

poll() // Example: Removing and returning the head of the queue
String firstBook = books.poll(); // removes and returns the first book

peek() // Example: Viewing the head of the queue without removing it
String firstBookView = books.peek(); // returns the first book without removing

isEmpty() // Example: Checking if the queue is empty
boolean isQueueEmpty = books.isEmpty(); // returns true or false

size() // Example: Checking how many books are in the queue
int numberOfBooks = books.size(); // returns the current count

remove() // Example: Removing the head of the queue
String firstBookRemoved = books.remove(); // removes and returns the head of the queue

contains(Object o) // Example: Checking if a specific book is in the queue
boolean hasBook = books.contains("1984"); // returns true or false

toArray() // Example: Converting the queue to an array
String[] bookArray = books.toArray(new String[0]); // converts to an array

iterator() // Example: Iterating through the queue
Iterator<String> it = books.iterator(); // creates an iterator for the queue
    ''', language="java")

    col2.subheader('HashSet')
    col2.code('''
add(E e) // Example: Adding a new book to the HashSet
HashSet<String> books = new HashSet<>();
books.add("The Great Gatsby");

remove(Object o) // Example: Removing a book from the HashSet
books.remove("The Great Gatsby"); // removes "The Great Gatsby"

contains(Object o) // Example: Checking if a specific book is in the HashSet
boolean hasBook = books.contains("1984"); // returns true or false

isEmpty() // Example: Checking if the HashSet is empty
boolean isSetEmpty = books.isEmpty(); // returns true or false

size() // Example: Checking how many books are in the HashSet
int numberOfBooks = books.size(); // returns the current count

clear() // Example: Clearing the HashSet
books.clear(); // removes all books from the HashSet

toArray() // Example: Converting the HashSet to an array
String[] bookArray = books.toArray(new String[0]); // converts to an array

iterator() // Example: Iterating through the HashSet
Iterator<String> it = books.iterator(); // creates an iterator for the HashSet

removeAll(Collection<?> c) // Example: Removing multiple books from the HashSet
books.removeAll(Arrays.asList("1984", "Moby Dick")); // removes specified books

retainAll(Collection<?> c) // Example: Retaining only specified books in the HashSet
books.retainAll(Arrays.asList("The Great Gatsby")); // keeps only "The Great Gatsby"
    ''', language="java")
