import streamlit as st

def ct_python_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Lower Bound')
        col1.code('''
# Finds the index of the first element in a sorted list that is
# greater than or equal to a specified target value using binary search.
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if valid(nums[mid], target):
            # Move the right pointer if the mid value is valid
            right = mid
        else:
            left = mid + 1
    return left

def valid(num, target):
    # Check if the current number meets the target condition
    return num >= target
    ''', language="python")

        col1.subheader('Trie')
        col1.code('''
class Trie:
    def __init__(self):
        # Initialize the Trie with an array for 26 lowercase letters
        self.children = [None] * 26
        self.end = False

    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            # Create a new Trie node if it doesn't exist for the character
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        # Mark the end of the word
        node.end = True

    def search(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            # Check if the character path exists and if it's the end of a word
            if not node.children[ch] or not node.children[ch].end:
                return False
            node = node.children[ch]
        return True
''', language="python")

        col1.subheader('Sliding Window (longest valid)')
        col1.code('''
def longest_valid(strings):
    res = 0
    right = 0
    # Use a set to track valid strings
    state = set()
    for i in range(len(strings)):
        state.add(strings[i])
        # While the state is not valid, remove strings from the right
        while not is_valid(state):
            state.remove(strings[right])
            right += 1

        res = max(res, i - right + 1)

    return res

def is_valid(state):
    # Implement your validation logic here
    # Return True if the state is valid, False otherwise
    pass
''', language="python")

        col1.subheader('Sliding Window (shortest valid)')
        col1.code('''
def shortest_valid(strings):
    res = len(strings) + 1
    right = 0
    # Use a set to track valid strings
    state = set()
    for i in range(len(strings)):
        state.add(strings[i])
        # While the state is valid, update the result and remove from the right
        while is_valid(state):
            res = min(res, i - right + 1)
            state.remove(strings[right])
            right += 1
    return -1 if (res == len(strings) + 1) else res

def is_valid(state):
    # Implement your validation logic here
    # Return True if the state is valid, False otherwise
    return True
''', language="python")

        col1.subheader('Monotone Stack (next greater)')
        col1.code('''
def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result
''', language="python")

        col1.subheader('BFS')
        col1.code('''
def bfs(graph, start):
    visited = set()
    queue = collections.deque([(start, 0)])

    while queue:
        node, level = queue.popleft()  # Dequeue a node and its level
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(f"Node: {node}, Level: {level}")  # Process the node
            # Enqueue all unvisited neighbors with the incremented level
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
    return
''', language="python")

        col1.subheader('Topological Sort')
        col1.code('''
from collections import defaultdict, deque

class Solution:
    def topological_sort(self, graph):
        indegree = defaultdict(int)
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        # Initialize the queue with nodes having 0 in-degree
        queue = deque([node for node in graph if indegree[node] == 0])
        while queue:
            node = queue.popleft()
            print(node)
            # Decrease the in-degree of neighbors
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
''', language="python")
