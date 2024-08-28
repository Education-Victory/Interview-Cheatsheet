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
        self.children = [None] * 26
        self.end = False

    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.end = True

    def _search_prefix(self, prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return
            node = node.children[ch]
        return node

    def search(self, word):
        node = self._search_prefix(word)
        return node and node.end

    def startsWith(self, prefix):
        return bool(self._search_prefix(prefix))
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

        col1.subheader('Union Find')
        col1.code('''
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
''', language="python")

        col1.subheader('Rolling Hash')
        col1.code('''
class RollingHash:
    def __init__(self, base=257, mod=10**9 + 7):
        self.base = base
        self.mod = mod
        self.hash_value = 0
        self.power = 1

    def compute_hash(self, s):
        self.hash_value = 0
        self.power = 1
        for char in s:
            self.hash_value = (self.hash_value * self.base + ord(char)) % self.mod
            self.power = (self.power * self.base) % self.mod
        return self.hash_value

    def roll_hash(self, old_char, new_char):
        self.hash_value = (self.hash_value * self.base - ord(old_char) * self.power + ord(new_char)) % self.mod
        if self.hash_value < 0:
            self.hash_value += self.mod
        return self.hash_value
''', language="python")
