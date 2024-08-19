import streamlit as st

def bif_java_columns():
    col1, col2 = st.columns(2)
    col1.subheader("String Manipulation");
    col1.code('''
    // Example: Initializing a string
    String text = "Hello, World!";

    // Example: Converting to uppercase
    String upperText = text.toUpperCase();  // returns "HELLO, WORLD!"

    // Example: Converting to lowercase
    String lowerText = text.toLowerCase();  // returns "hello, world!"

    // Example: Replacing a substring
    String replacedText = text.replace("World", "Java");  // returns "Hello, Java!"

    // Example: Splitting a string into an array
    String[] words = text.split(", ");  // returns ["Hello", "World!"]

    // Example: Joining an array into a string (using String.join)
    String joinedText = String.join(" - ", words);  // returns "Hello - World!"

    // Example: Checking if a string starts with a substring
    boolean startsWithHello = text.startsWith("Hello");  // returns true

    // Example: Checking if a string ends with a substring
    boolean endsWithExclamation = text.endsWith("!");  // returns true

    // Example: Stripping whitespace from a string
    String whitespaceText = "   Hello, World!   ";
    String strippedText = whitespaceText.trim();  // returns "Hello, World!"
    ''', language="java");

    col1.subheader("Sorting");
    col1.code('''
    import java.util.Arrays;
    import java.util.Comparator;

    // Example: Sorting an array of integers
    int[] sortedArray = {3, 1, 4, 2};
    Arrays.sort(sortedArray);  // Output: [1, 2, 3, 4]

    // Example: Sorting an array of strings by length
    String[] sortedByLength = {"apple", "banana", "kiwi"};
    Arrays.sort(sortedByLength, Comparator.comparingInt(String::length));  // Output: ["kiwi", "apple", "banana"]

    // Example: Sorting an array in descending order
    Integer[] sortedDesc = {5, 2, 9, 1};
    Arrays.sort(sortedDesc, Comparator.reverseOrder());  // Output: [9, 5, 2, 1]

    // Example: Sorting an array of tuples (using a 2D array)
    String[][] tuples = {{ "1", "b" }, { "2", "a" }, { "3", "c" }};
    Arrays.sort(tuples, Comparator.comparing(a -> a[1]));  // Output: [["2", "a"], ["1", "b"], ["3", "c"]]

    // Example: Sorting a list of maps by a key
    List<Map<String, Object>> dicts = new ArrayList<>();
    dicts.add(Map.of("name", "Alice", "age", 30));
    dicts.add(Map.of("name", "Bob", "age", 25));
    dicts.sort(Comparator.comparingInt(d -> (int) d.get("age")));  // Output: [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]

    // Example: Sorting with a custom comparator
    List<Integer[]> myListCustom = Arrays.asList(new Integer[]{2, 3}, new Integer[]{1, 4}, new Integer[]{5, 2});
    myListCustom.sort(Comparator.comparingInt(a -> a[1] - a[0]));  // Output: [[2, 3], [1, 4], [5, 2]]

    // Example: Sorting in descending order using a custom key
    myListCustom.sort(Comparator.comparingInt(a -> a[1]).reversed());  // Output: [[5, 2], [2, 3], [1, 4]]
    ''', language="java");

    col2.subheader("Bit Manipulation");
    col2.code('''
    // Example: Check if a number is even or odd
    int num = 5;
    boolean isEven = (num & 1) == 0;  // Output: false

    // Example: Set a bit at a specific position
    int bitPosition = 2;
    num = 5;  // Binary: 101
    num |= (1 << bitPosition);  // Set the bit at position 2
    // num now is 7 (Binary: 111)

    // Example: Clear a bit at a specific position
    num = 7;  // Binary: 111
    num &= ~(1 << bitPosition);  // Clear the bit at position 2
    // num now is 5 (Binary: 101)

    // Example: Toggle a bit at a specific position
    num = 5;  // Binary: 101
    num ^= (1 << bitPosition);  // Toggle the bit at position 2
    // num now is 7 (Binary: 111)

    // Example: Check if a bit is set at a specific position
    boolean isSet = (num & (1 << bitPosition)) != 0;  // Output: true

    // Example: Count the number of set bits (Hamming Weight)
    int count = 0;
    num = 7;  // Binary: 111
    while (num != 0) {
        count += num & 1;
        num >>= 1;
    }
    // count now is 3

    // Example: Get the rightmost set bit
    num = 10;  // Binary: 1010
    int rightmostSetBit = num & -num;  // Output: 2 (Binary: 10)

    // Example: Calculate if a number is a power of two
    num = 8;
    boolean isPowerOfTwo = (num > 0) && (num & (num - 1)) == 0;  // Output: true

    // Example: Clear the last set bit
    num = 10;  // Binary: 1010
    num &= (num - 1);  // Clears the rightmost set bit
    // num now is 8 (Binary: 1000)
    ''', language="java");

    col1.subheader("Set Operations");
    col1.code('''
    import java.util.HashSet;
    import java.util.Set;

    // Example: Set operations - union
    Set<Integer> setA = new HashSet<>(Set.of(1, 2, 3));
    Set<Integer> setB = new HashSet<>(Set.of(3, 4, 5));
    Set<Integer> union = new HashSet<>(setA);
    union.addAll(setB);  // Output: {1, 2, 3, 4, 5}

    // Example: Set operations - intersection
    Set<Integer> intersection = new HashSet<>(setA);
    intersection.retainAll(setB);  // Output: {3}

    // Example: Set operations - difference
    Set<Integer> difference = new HashSet<>(setA);
    difference.removeAll(setB);  // Output: {1, 2}

    // Example: Set operations - symmetric difference
    Set<Integer> symmetricDifference = new HashSet<>(setA);
    symmetricDifference.addAll(setB);
    Set<Integer> temp = new HashSet<>(setA);
    temp.retainAll(setB);
    symmetricDifference.removeAll(temp);  // Output: {1, 2, 4, 5}

    // Example: Set operations - subset
    Set<Integer> setC = new HashSet<>(Set.of(1, 2));
    boolean isSubset = setC.stream().allMatch(setA::contains);  // Output: true

    // Example: Set operations - superset
    boolean isSuperset = setA.containsAll(setC);  // Output: true
    ''', language="java");

    col2.subheader("Pow Function");
    col2.code('''
    // Example: Using Math.pow to calculate a power
    double powerResult = Math.pow(2, 3);  // Output: 8.0 (2^3)

    // Example: Using Math.pow with a negative exponent
    double negativeExponent = Math.pow(2, -2);  // Output: 0.25 (1/(2^2))

    // Example: Modulus power calculation (not directly supported in Math.pow)
    // Using a custom method to calculate (base^exponent) % modulus
    public static int powMod(int base, int exponent, int modulus) {
        int result = 1;
        base = base % modulus;
        while (exponent > 0) {
            if ((exponent & 1) == 1) {  // If exponent is odd
                result = (result * base) % modulus;
            }
            exponent >>= 1;  // Divide exponent by 2
            base = (base * base) % modulus;  // Square the base
        }
        return result;
    }
    int modulusPower = powMod(3, 2, 5);  // Output: 4 (3^2 % 5)
    ''', language="java");

    col2.subheader("Math Library");
    col2.code('''
    // Example: Calculate the sine of an angle (in radians)
    double sineValue = Math.sin(Math.PI / 2);  // Output: 1.0

    // Example: Find the logarithm (base 10)
    double logarithmValue = Math.log10(100);  // Output: 2.0

    // Example: Find the natural logarithm
    double naturalLogValue = Math.log(Math.E);  // Output: 1.0

    // Example: Return the ceiling of x
    double roundedValueCeil = Math.ceil(4.2);  // Output: 5.0

    // Example: Return the floor of x
    double roundedValueFloor = Math.floor(4.2);  // Output: 4.0

    // Example: Calculate the greatest common divisor (GCD)
    int gcdValue = gcd(48, 18);  // Output: 6

    // Helper method for GCD
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    ''', language="java");
