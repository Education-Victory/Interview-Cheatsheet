import streamlit as st

def bif_python_columns():
    col1, col2 = st.columns(2)
    col1.subheader('String Manipulation')
    col1.code('''
    # Example: Initializing a string
    text = "Hello, World!"

    # Example: Converting to uppercase
    upper_text = text.upper()  # returns "HELLO, WORLD!"

    # Example: Converting to lowercase
    lower_text = text.lower()  # returns "hello, world!"

    # Example: Replacing a substring
    replaced_text = text.replace("World", "Python")  # returns "Hello, Python!"

    # Example: Splitting a string into a list
    words = text.split(", ")  # returns ["Hello", "World!"]

    # Example: Joining a list into a string
    joined_text = " - ".join(words)  # returns "Hello - World!"

    # Example: Checking if a string starts with a substring
    starts_with_hello = text.startswith("Hello")  # returns True

    # Example: Checking if a string ends with a substring
    ends_with_exclamation = text.endswith("!")  # returns True

    # Example: Stripping whitespace from a string
    whitespace_text = "   Hello, World!   "
    stripped_text = whitespace_text.strip()  # returns "Hello, World!"
    ''', language="python")

    col1.subheader('Sorting')
    col1.code('''
    # Example: Sorting a list of integers
    sorted_list_integers = sorted([3, 1, 4, 2])  # Output: [1, 2, 3, 4]

    # Example: Sorting a list of strings by length
    sorted_by_length = sorted(["apple", "banana", "kiwi"], key=len)  # Output: ['kiwi', 'apple', 'banana']

    # Example: Sorting a list in descending order
    sorted_desc = sorted([5, 2, 9, 1], reverse=True)  # Output: [9, 5, 2, 1]

    # Example: Sorting a list of tuples by the second element
    tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

    # Example: Sorting a list of dictionaries by a key
    dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    sorted_dicts = sorted(dicts, key=lambda x: x['age'])  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]

    # Example: Sorting a list of dictionaries by a custom key
    my_list = [{'name': 'Charlie', 'score': 85}, {'name': 'Alice', 'score': 90}]
    sorted_by_score = sorted(my_list, key=lambda x: x['score'])  # Output: [{'name': 'Charlie', 'score': 85}, {'name': 'Alice', 'score': 90}]

    # Example: Sorting with a custom function
    def custom_sort(x):
        return x[1] - x[0]

    my_list_custom = [(2, 3), (1, 4), (5, 2)]
    sorted_custom = sorted(my_list_custom, key=custom_sort)  # Output: [(2, 3), (1, 4), (5, 2)]

    # Example: Sorting in descending order using a custom key
    sorted_desc_custom = sorted(my_list, key=lambda x: x['score'], reverse=True)  # Output: [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]
    ''', language="python")

    col1.subheader('Bit Manipulation')
    col1.code('''
    # Example: Check if a number is even or odd
    num = 5
    is_even = (num & 1) == 0  # Output: False

    # Example: Set a bit at a specific position
    bit_position = 2
    num = 5  # Binary: 101
    num |= (1 << bit_position)  # Set the bit at position 2
    # num now is 7 (Binary: 111)

    # Example: Clear a bit at a specific position
    num = 7  # Binary: 111
    num &= ~(1 << bit_position)  # Clear the bit at position 2
    # num now is 5 (Binary: 101)

    # Example: Toggle a bit at a specific position
    num = 5  # Binary: 101
    num ^= (1 << bit_position)  # Toggle the bit at position 2
    # num now is 7 (Binary: 111)

    # Example: Check if a bit is set at a specific position
    is_set = (num & (1 << bit_position)) != 0  # Output: True

    # Example: Count the number of set bits (Hamming Weight)
    count = 0
    num = 7  # Binary: 111
    while num:
        count += num & 1
        num >>= 1
    # count now is 3

    # Example: Get the rightmost set bit
    num = 10  # Binary: 1010
    rightmost_set_bit = num & -num  # Output: 2 (Binary: 10)

    # Example: Calculate if a number is a power of two
    num = 8
    is_power_of_two = (num > 0) and (num & (num - 1)) == 0  # Output: True

    # Example: Clear the last set bit
    num = 10  # Binary: 1010
    num &= (num - 1)  # Clears the rightmost set bit
    # num now is 8 (Binary: 1000)
    ''', language="python")

    col1.subheader('Strip Operations')
    col1.code('''
    # Example: Strip whitespace from both ends
    stripped = "   hello   ".strip()  # Output: 'hello'

    # Example: Strip specific characters
    stripped_chars = "---hello---".strip('-')  # Output: 'hello'

    # Example: Strip only leading whitespace
    leading_strip = "   hello".lstrip()  # Output: 'hello'

    # Example: Strip only trailing whitespace
    trailing_strip = "hello   ".rstrip()  # Output: 'hello'
    ''', language="python")

    col2.subheader('Set Operations')
    col2.code('''
    # Example: Set operations - union
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    union = set_a | set_b  # Output: {1, 2, 3, 4, 5}

    # Example: Set operations - intersection
    intersection = set_a & set_b  # Output: {3}

    # Example: Set operations - difference
    difference = set_a - set_b  # Output: {1, 2}

    # Example: Set operations - symmetric difference
    symmetric_difference = set_a ^ set_b  # Output: {1, 2, 4, 5}

    # Example: Set operations - subset
    set_c = {1, 2}
    is_subset = set_c <= set_a  # Output: True

    # Example: Set operations - superset
    is_superset = set_a >= set_c  # Output: True
    ''', language="python")

    col2.subheader('Slicing Operations')
    col2.code('''
    # Example: Reversing a list using slice
    reversed_list = my_list[::-1]  # Output: [5, 4, 3, 2, 1, 0]

    # Example: Slicing a list to get the last three elements
    last_three = my_list[-3:]  # Output: [3, 4, 5]

    # Example: Slicing a string to get every second character
    every_second_char = "abcdef"[::2]  # Output: 'ace'

    # Example 9: Slicing a list with negative indices
    negative_index_slice = my_list[-4:-1]  # Output: [2, 3, 4]
    ''', language="python")

    col2.subheader('Pow Function')
    col2.code('''
    # Example: Using pow to calculate a power
    power_result = pow(2, 3)  # Output: 8 (2^3)

    # Example: Using pow with a negative exponent
    negative_exponent = pow(2, -2)  # Output: 0.25 (1/(2^2))

    # Example: Using pow for multiple arguments (base, exponent, modulus)
    modulus_power = pow(3, 2, 5)  # Output: 4 (3^2 % 5)
    ''', language="python")

    col2.subheader('Math Library')
    col2.code('''
    import math
    # Example: Calculate the sine of an angle (in radians)
    sine_value = math.sin(math.pi / 2)  # Output: 1.0

    # Example: Find the logarithm (base 10)
    logarithm_value = math.log10(100)  # Output: 2.0

    # Example: Find the natural logarithm
    natural_log_value = math.log(math.e)  # Output: 1.0

    # Example: Calculate the greatest common divisor (GCD)
    gcd_value = math.gcd(48, 18)  # Output: 6

    # Example: Return the ceiling of x, the smallest integer greater than or equal to x
    rounded_value = math.ceil(4.2)  # Output: 5

    # Example: Return the floor of x, the largest integer less than or equal to x
    rounded_value = math.floor(4.2)  # Output: 4
    ''', language="python")

    col2.subheader('Code Snippets')
    col2.code('''
    # Example: Filtering with List Comprehension
    filtered_list = [x for x in my_list if x > threshold]

    # Example: Finding Unique Elements
    unique_elements = list(set(my_list))  # returns unique elements from my_list

    # Example: Rotating a List
    rotated_list = my_list[k:] + my_list[:k]  # Rotate right by k

    # Example: Flattening a Nested List
    flattened = [item for sublist in my_nested_list for item in sublist]  # flattens the nested list

    # Example: Checking for Duplicates
    has_duplicates = len(my_list) != len(set(my_list))  # returns True if there are duplicates

    # Example: Generating a Range of Numbers
    range_list = list(range(start, end, step))  # generates a list of numbers from start to end with a given step
    ''', language="python")

    col2.subheader("Random Library");
    col2.code('''
        # Return a random number between min and max
        min_val = 5
        max_val = 15
        random_in_range = random.randint(min_val, max_val)

        # Return a random number between 1 and 10
        n = 10
        random_number = random.randint(1, n)

        # Return a random double between 0.0 and 1.0
        random_double = random.random()

        # Return a random boolean value (True or False)
        random_boolean = random.choice([True, False])
        ''', language="python");
