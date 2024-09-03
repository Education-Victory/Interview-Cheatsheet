import streamlit as st

def sa_python_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Morris Traversal')
        col1.code('''
# Leetcode 94: Binary Tree Inorder Traversal
def inorder_traversal(self, root):
    current = root
    result = []

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find the inorder predecessor of current
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            # Make current as right child of its predecessor
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                # Revert the changes made to restore the original tree
                predecessor.right = None
                result.append(current.val)
                current = current.right
    return result

# Example usage
# Constructing a simple binary tree
#       1
#      / \\
#     2   3
#    / \\
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(morris_traversal(root))  # Output: [4, 2, 5, 1, 3]
''', language="python")

        col1.subheader('Floyd\'s Cycle Detection Algorithm')
        col1.code('''
# Leetcode 141: Linked List Cycle
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head:
        return False

    tortoise = head
    hare = head

    while hare and hare.next:
        # Move tortoise by 1
        tortoise = tortoise.next
        # Move hare by 2
        hare = hare.next.next
        # Cycle detected
        if tortoise == hare:
            return True
    # No cycle
    return False

# Example usage
# Creating a linked list with a cycle
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |_________|
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# Creating a cycle
head.next.next.next.next = head.next
# Output: True
print(has_cycle(head))
''', language="python")


        col1.subheader('Boyer–Moore majority vote algorithm')
        col1.code('''
# Leetcode 169: Majority Element
def boyer_moore_majority_vote(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify that the candidate is indeed the majority element
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

# Example usage
nums = [3, 2, 3]
print(boyer_moore_majority_vote(nums))  # Output: 3
''', language="python")

        col1.subheader('Reversal algorithm for array rotation')
        col1.code('''
# Leetcode 189: Rotate Array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d >= n
    reverse(arr, 0, d - 1)       # Step 1: Reverse the first d elements
    reverse(arr, d, n - 1)       # Step 2: Reverse the remaining elements
    reverse(arr, 0, n - 1)       # Step 3: Reverse the entire array

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
rotate(arr, d)
# Output: [4, 5, 6, 7, 1, 2, 3]
print(arr)
''', language="python")

        col1.subheader('Fast Power Algorithm')
        col1.code('''
# Leetcode 50: Pow(x, n)
def fast_power(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

# Example usage
x = 2.0
n = 10
# Output: 1024.0
print(fast_power(x, n))
''', language="python")

        col1.subheader('Quick Select Algorithm')
        col1.code('''
# Leetcode 215: Kth Largest Element in an Array
import random

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    # Move pivot to end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Move pivot to its final place
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

def quickselect(arr, left, right, k):
    # Base case: only one element
    if left == right:
        return arr[left]

    pivot_index = random.randint(left, right)
    pivot_index = partition(arr, left, right, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)

# Example usage
arr = [3, 2, 1, 5, 4]
k = 2  # Looking for the 3rd smallest element (index 2)
result = quickselect(arr, 0, len(arr) - 1, k)
# Output: 3
print(result)
''', language="python")

        col1.subheader('Count Primes Algorithm')
        col1.code('''
# Leetcode 204: Count Primes
def count_primes(n):
    if n <= 2:
        return 0
    # Initialize a list of boolean values
    primes = [True] * n
    # 0 and 1 are not prime numbers
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            # Mark all multiples of p as False
            for i in range(p * p, n, p):
                primes[i] = False
    # Count the number of True values in the list
    return sum(primes)

n = 30
print(count_primes(n))  # Output: 10
''', language="python")

