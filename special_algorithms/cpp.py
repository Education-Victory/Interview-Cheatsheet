import streamlit as st

def sa_cpp_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Morris Traversal')
        col1.code('''
// Leetcode 94: Binary Tree Inorder Traversal
#include <iostream>

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void inorderTraversal(TreeNode* root) {
    TreeNode* current = root;

    while (current != nullptr) {
        if (current->left == nullptr) {
            std::cout << current->val << " ";
            current = current->right;
        } else {
            // Find the inorder predecessor of current
            TreeNode* predecessor = current->left;
            while (predecessor->right != nullptr && predecessor->right != current) {
                predecessor = predecessor->right;
            }

            // Make current as right child of its predecessor
            if (predecessor->right == nullptr) {
                predecessor->right = current;
                current = current->left;
            } else {
                // Revert the changes made to restore the original tree
                predecessor->right = nullptr;
                std::cout << current->val << " ";
                current = current->right;
            }
        }
    }
}

int main() {
    // Constructing a simple binary tree
    //       1
    //      / \\
    //     2   3
    //    / \\
    //   4   5
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    inorderTraversal(root);  // Output: 4 2 5 1 3

    return 0;
}
''', language="cpp")

        col1.subheader('Floyd\'s Cycle Detection Algorithm')
        col1.code('''
// Leetcode 141: Linked List Cycle
#include <iostream>

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int x) : val(x), next(nullptr) {}
};

bool hasCycle(ListNode* head) {
    if (!head) {
        return false;
    }

    ListNode* tortoise = head;
    ListNode* hare = head;

    while (hare != nullptr && hare->next != nullptr) {
        // Move tortoise by 1
        tortoise = tortoise->next;
        // Move hare by 2
        hare = hare->next->next;

        // Cycle detected
        if (tortoise == hare) {
            return true;
        }
    }

    // No cycle
    return false;
}

int main() {
    // Creating a linked list with a cycle
    // 1 -> 2 -> 3 -> 4
    //      ^         |
    //      |_________|
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    // Creating a cycle
    head->next->next->next->next = head->next;
    // Output: true
    std::cout << std::boolalpha << hasCycle(head) << std::endl;

    return 0;
}
''', language="cpp")

        col1.subheader('Boyer–Moore majority vote algorithm')
        col1.code('''
// Leetcode 169: Majority Element
#include <iostream>
#include <vector>

int boyerMooreMajorityVote(const std::vector<int>& nums) {
    int candidate = 0;
    int count = 0;

    for (int num : nums) {
        if (count == 0) {
            candidate = num;
            count = 1;
        } else if (num == candidate) {
            count++;
        } else {
            count--;
        }
    }

    // Verify that the candidate is indeed the majority element
    count = 0;
    for (int num : nums) {
        if (num == candidate) {
            count++;
        }
    }
    // Return -1 if no majority element
    return count > nums.size() / 2 ? candidate : -1;
}

int main() {
    std::vector<int> nums = {3, 2, 3};
    // Output: 3
    std::cout << boyerMooreMajorityVote(nums) << std::endl;
    return 0;
}
''', language="cpp")

        col1.subheader('Reversal algorithm for array rotation')
        col1.code('''
// Leetcode 189: Rotate Array
#include <iostream>
#include <vector>

void reverse(std::vector<int>& arr, int start, int end) {
    while (start < end) {
        std::swap(arr[start], arr[end]);
        start++;
        end--;
    }
}

void rotate(std::vector<int>& arr, int d) {
    int n = arr.size();
    d = d % n;  // Handle cases where d >= n
    reverse(arr, 0, d - 1);   // Step 1: Reverse the first d elements
    reverse(arr, d, n - 1);   // Step 2: Reverse the remaining elements
    reverse(arr, 0, n - 1);   // Step 3: Reverse the entire array
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    int d = 3;
    rotate(arr, d);
    for (int num : arr) {
        // Output: 4 5 6 7 1 2 3
        std::cout << num << " ";
    }
    return 0;
}
''', language="cpp")

        col1.subheader('Fast Power Algorithm')
        col1.code('''
// Leetcode 50: Pow(x, n)
#include <iostream>

double fastPower(double x, int n) {
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    double result = 1;
    while (n > 0) {
        if (n % 2 == 1) {  // If n is odd
            result *= x;
        }
        x *= x;  // Square the base
        n /= 2;  // Divide n by 2
    }
    return result;
}

int main() {
    double x = 2.0;
    int n = 10;
    std::cout << fastPower(x, n) << std::endl;  // Output: 1024.0
    return 0;
}
''', language="cpp")

        col1.subheader('Quick Select Algorithm')
        col1.code('''
// Leetcode 215: Kth Largest Element in an Array
#include <iostream>
#include <vector>
#include <cstdlib>

int partition(std::vector<int>& arr, int left, int right, int pivotIndex) {
    int pivotValue = arr[pivotIndex];
    // Move pivot to end
    std::swap(arr[pivotIndex], arr[right]);
    int storeIndex = left;

    for (int i = left; i < right; i++) {
        if (arr[i] < pivotValue) {
            std::swap(arr[storeIndex], arr[i]);
            storeIndex++;
        }
    }

    // Move pivot to its final place
    std::swap(arr[storeIndex], arr[right]);
    return storeIndex;
}

int quickSelect(std::vector<int>& arr, int left, int right, int k) {
    if (left == right) {  // Base case: only one element
        return arr[left];
    }

    int pivotIndex = left + rand() % (right - left + 1);
    pivotIndex = partition(arr, left, right, pivotIndex);

    if (k == pivotIndex) {
        return arr[k];
    } else if (k < pivotIndex) {
        return quickSelect(arr, left, pivotIndex - 1, k);
    } else {
        return quickSelect(arr, pivotIndex + 1, right, k);
    }
}

int main() {
    std::srand(std::time(0)); // Seed for random number generation
    std::vector<int> arr = {3, 2, 1, 5, 4};
    int k = 2;  // Looking for the 3rd smallest element (index 2)
    int result = quickSelect(arr, 0, arr.size() - 1, k);
    std::cout << result << std::endl;  // Output: 3
    return 0;
}
''', language="cpp")

        col1.subheader('Count Primes Algorithm')
        col1.code('''
// Leetcode 204: Count Primes
#include <iostream>
#include <vector>

int countPrimes(int n) {
    if (n <= 2) {
        return 0;  // There are no prime numbers less than 2
    }

    std::vector<bool> primes(n, true); // Initialize a boolean vector
    primes[0] = primes[1] = false; // 0 and 1 are not prime numbers

    for (int p = 2; p * p < n; p++) {
        if (primes[p]) {
            // Mark all multiples of p as false
            for (int i = p * p; i < n; i += p) {
                primes[i] = false;
            }
        }
    }

    // Count the number of true values
    int count = 0;
    for (int p = 2; p < n; p++) {
        if (primes[p]) {
            count++;
        }
    }
    return count;
}

int main() {
    int n = 30;
    std::cout << countPrimes(n) << std::endl;  // Output: 10
    return 0;
}
''', language="java")

