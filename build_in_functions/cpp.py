import streamlit as st

def bif_cpp_columns():
    col1, col2 = st.columns(2)
    col1.subheader("String Manipulation");
    col1.code('''
    // Example: Initializing a string
    string text = "Hello, World!";

    // Example: Converting to uppercase
    string upper_text = text;
    transform(upper_text.begin(), upper_text.end(), upper_text.begin(), ::toupper);  // Output: "HELLO, WORLD!"

    // Example: Converting to lowercase
    string lower_text = text;
    transform(lower_text.begin(), lower_text.end(), lower_text.begin(), ::tolower);  // Output: "hello, world!"

    // Example: Replacing a substring
    size_t pos = text.find("World");
    if (pos != string::npos) {
        text.replace(pos, 5, "C++");  // Output: "Hello, C++!"
    }

    // Example: Splitting a string into a vector
    stringstream ss(text);
    string word;
    vector<string> words;
    while (getline(ss, word, ',')) {
        words.push_back(word);
    }  // Output: ["Hello", " World!"]

    // Example: Joining a vector into a string
    string joined_text = "";
    for (const auto& w : words) {
        joined_text += w + " - ";  // Output: "Hello -  World! - "
    }
    joined_text = joined_text.substr(0, joined_text.length() - 3);  // Remove last " - "

    // Example: Checking if a string starts with a substring
    bool starts_with_hello = text.rfind("Hello", 0) == 0;  // Output: true

    // Example: Checking if a string ends with a substring
    bool ends_with_exclamation = text.back() == '!';  // Output: true
    )''', language="cpp");

    col1.subheader("Sorting");
    col1.code('''
    // Example: Sorting a vector of integers
    vector<int> sorted_list_integers = {3, 1, 4, 2};
    sort(sorted_list_integers.begin(), sorted_list_integers.end());  // Output: [1, 2, 3, 4]

    // Example: Sorting a vector of strings by length
    vector<string> sorted_by_length = {"apple", "banana", "kiwi"};
    sort(sorted_by_length.begin(), sorted_by_length.end(), [](const string &a, const string &b) {
        return a.length() < b.length();
    });  // Output: ["kiwi", "apple", "banana"]

    // Example: Sorting a vector in descending order
    vector<int> sorted_desc = {5, 2, 9, 1};
    sort(sorted_desc.begin(), sorted_desc.end(), greater<int>());  // Output: [9, 5, 2, 1]

    // Example: Sorting a vector of tuples by the second element
    vector<tuple<int, char>> tuples = {{1, 'b'}, {2, 'a'}, {3, 'c'}};
    sort(tuples.begin(), tuples.end(), [](const tuple<int, char> &a, const tuple<int, char> &b) {
        return get<1>(a) < get<1>(b);
    });  // Output: [(2, 'a'), (1, 'b'), (3, 'c')]

    // Example: Sorting a vector of maps by a key
    vector<map<string, int>> dicts = { { "name", "Alice", "age", 30 }, { "name", "Bob", "age", 25 } };
    sort(dicts.begin(), dicts.end(), [](const map<string, int> &a, const map<string, int> &b) {
        return a.at("age") < b.at("age");
    });  // Output: [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]

    // Example: Sorting with a custom function
    vector<pair<int, int>> my_list_custom = {{2, 3}, {1, 4}, {5, 2}};
    sort(my_list_custom.begin(), my_list_custom.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
        return (a.second - a.first) < (b.second - b.first);
    });  // Output: [(2, 3), (1, 4), (5, 2)]

    // Example: Sorting in descending order using a custom key
    sort(my_list_custom.begin(), my_list_custom.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
        return a.second > b.second;
    });  // Output: [(5, 2), (2, 3), (1, 4)]
    )''', language="cpp");

    col1.subheader("Bit Manipulation");
    col1.code('''
    // Example: Check if a number is even or odd
    int num = 5;
    bool is_even = (num & 1) == 0;  // Output: false

    // Example: Set a bit at a specific position
    int bit_position = 2;
    num = 5;  // Binary: 101
    num |= (1 << bit_position);  // Set the bit at position 2
    // num now is 7 (Binary: 111)

    // Example: Clear a bit at a specific position
    num = 7;  // Binary: 111
    num &= ~(1 << bit_position);  // Clear the bit at position 2
    // num now is 5 (Binary: 101)

    // Example: Toggle a bit at a specific position
    num = 5;  // Binary: 101
    num ^= (1 << bit_position);  // Toggle the bit at position 2
    // num now is 7 (Binary: 111)

    // Example: Check if a bit is set at a specific position
    bool is_set = (num & (1 << bit_position)) != 0;  // Output: true

    // Example: Count the number of set bits (Hamming Weight)
    int count = 0;
    num = 7;  // Binary: 111
    while (num) {
        count += num & 1;
        num >>= 1;
    }
    // count now is 3

    // Example: Get the rightmost set bit
    num = 10;  // Binary: 1010
    int rightmost_set_bit = num & -num;  // Output: 2 (Binary: 10)

    // Example: Calculate if a number is a power of two
    num = 8;
    bool is_power_of_two = (num > 0) && ((num & (num - 1)) == 0);  // Output: true

    // Example: Clear the last set bit
    num = 10;  // Binary: 1010
    num &= (num - 1);  // Clears the rightmost set bit
    // num now is 8 (Binary: 1000)
    ''', language="cpp");

    col1.subheader("Strip Operations");
    col1.code('''
    // Example: Strip whitespace from both ends
    string stripped = "   hello   ";
    stripped.erase(0, stripped.find_first_not_of(" "));  // Remove leading whitespace
    stripped.erase(stripped.find_last_not_of(" ") + 1);  // Remove trailing whitespace
    // Output: "hello"

    // Example: Strip specific characters
    string stripped_chars = "---hello---";
    stripped_chars.erase(0, stripped_chars.find_first_not_of('-'));  // Remove leading '-'
    stripped_chars.erase(stripped_chars.find_last_not_of('-') + 1);  // Remove trailing '-'
    // Output: "hello"

    // Example: Strip only leading whitespace
    string leading_strip = "   hello";
    leading_strip.erase(0, leading_strip.find_first_not_of(" "));  // Output: "hello"

    // Example: Strip only trailing whitespace
    string trailing_strip = "hello   ";
    trailing_strip.erase(trailing_strip.find_last_not_of(" ") + 1);  // Output: "hello"
    ''', language="cpp");

    col2.subheader("Set Operations");
    col2.code('''
    // Example: Set operations - union
    set<int> set_a = {1, 2, 3};
    set<int> set_b = {3, 4, 5};
    set<int> union_set;
    set_union(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(), inserter(union_set, union_set.begin()));
    // Output: {1, 2, 3, 4, 5}

    // Example: Set operations - intersection
    set<int> intersection_set;
    set_intersection(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(), inserter(intersection_set, intersection_set.begin()));
    // Output: {3}

    // Example: Set operations - difference
    set<int> difference_set;
    set_difference(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(), inserter(difference_set, difference_set.begin()));
    // Output: {1, 2}

    // Example: Set operations - symmetric difference
    set<int> symmetric_difference_set;
    set_symmetric_difference(set_a.begin(), set_a.end(), set_b.begin(), set_b.end(), inserter(symmetric_difference_set, symmetric_difference_set.begin()));
    // Output: {1, 2, 4, 5}

    // Example: Set operations - subset
    set<int> set_c = {1, 2};
    bool is_subset = includes(set_a.begin(), set_a.end(), set_c.begin(), set_c.end());  // Output: true

    // Example: Set operations - superset
    bool is_superset = includes(set_a.begin(), set_a.end(), set_c.begin(), set_c.end());  // Output: true
    ''', language="cpp");

    col2.subheader("Slicing Operations");
    col2.code('''
    // Example: Reversing a vector
    vector<int> my_list = {0, 1, 2, 3, 4, 5};
    reverse(my_list.begin(), my_list.end());  // Output: [5, 4, 3, 2, 1, 0]

    // Example: Slicing a vector to get the last three elements
    vector<int> last_three(my_list.end() - 3, my_list.end());  // Output: [3, 4, 5]

    // Example: Slicing a vector with negative indices (manual implementation)
    vector<int> negative_index_slice(my_list.end() - 4, my_list.end() - 1);  // Output: [2, 3, 4]
    ''', language="cpp");

    col2.subheader("Pow Function");
    col2.code('''
    // Example: Using pow to calculate a power
    double power_result = pow(2, 3);  // Output: 8

    // Example: Using pow with a negative exponent
    double negative_exponent = pow(2, -2);  // Output: 0.25

    // Example: Using pow for multiple arguments (base, exponent, modulus)
    int base = 3, exponent = 2, modulus = 5;
    int modulus_power = static_cast<int>(pow(base, exponent)) % modulus;  // Output: 4
    ''', language="cpp");

    col2.subheader("Math Library Examples");
    col2.code('''
    // Example: Calculate the sine of an angle (in radians)
    double sine_value = sin(M_PI / 2);  // Output: 1.0

    // Example: Find the logarithm (base 10)
    double logarithm_value = log10(100);  // Output: 2.0

    // Example: Find the natural logarithm
    double natural_log_value = log(M_E);  // Output: 1.0

    // Example: Calculate the greatest common divisor (GCD)
    int gcd_value = __gcd(48, 18);  // Output: 6

    // Example: Return the ceiling of x
    double rounded_value_ceil = ceil(4.2);  // Output: 5.0

    // Example: Return the floor of x
    double rounded_value_floor = floor(4.2);  // Output: 4.0
    ''', language="cpp");
