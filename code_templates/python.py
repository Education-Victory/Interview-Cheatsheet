import streamlit as st
from openai import OpenAI

def ct_python_columns():
    col1, col2 = st.columns(2)

    code_sections = [
        {
            "header": "Lower Bound",
            "code": '''
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
    '''
        },
        {
            "header": "Trie",
            "code": '''
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
    '''
        },
        {
            "header": "Sliding Window (longest valid)",
            "code": '''
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
    '''
        },
        {
            "header": "Sliding Window (shortest valid)",
            "code": '''
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
    '''
        },
        {
            "header": "Monotone Stack (next greater)",
            "code": '''
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
    '''
        },
        {
            "header": "BFS",
            "code": '''
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
    '''
        },
        {
            "header": "Topological Sort",
            "code": '''
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
    '''
        },
        {
            "header": "Union Find",
            "code": '''
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
    '''
        },
        {
            "header": "Rolling Hash",
            "code": '''
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
    '''
        }
    ]

    # keep track of current section
    if 'section_index' not in st.session_state:
        st.session_state.section_index = 0

    if 'pycodes' not in st.session_state:
        st.session_state.pycodes = code_sections

    def display_code():
        st.subheader(st.session_state.pycodes[st.session_state.section_index]["header"])
        if not hide:
            st.code(st.session_state.pycodes[st.session_state.section_index]["code"], language="python")
        else:
            st.code("Code template hidden.")

    def next_code():
        if st.session_state.section_index + 1 >= len(st.session_state.pycodes):
            st.session_state.section_index = 0
        else:
            st.session_state.section_index += 1

    def previous_code():
        if st.session_state.section_index > 0:
            st.session_state.section_index -= 1

    client = OpenAI(
        api_key="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",
    )

    prompt = "You are a programming assistant. You are provided with a programming concept followed by a code snippet. " \
             "Your task is to check the following: 1. Syntax Validity: Ensure the code has no syntax errors. " \
             "2. Concept Implementation: Verify if the code approximately follows the right way of implementing " \
             "the given concept. Respond with one of the following ONLY: 'Valid Code' if both criteria are satisfied." \
             "'Syntax Error' if there are syntax errors in the code. 'Needs Improvement' if the code is not correctly " \
             "implementing the concept."
    def check_syntax(header, code):
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a programming assistant."},
                {"role": "user", "content": prompt + "\n\n" + header + "\n\n" + code}
            ],
            model="gpt-3.5-turbo",
            max_tokens=2
        )
        return response.choices[0].message.content.strip()

    hide = st.checkbox("Hide code", key="python_hide")
    # Display the current code section in the first column
    with col1:
        display_code()
        button_1, _, button_2, = st.columns([1, 2.7, 1])

        if button_1.button("Previous", key="python_prev", on_click=previous_code):
            pass

        if button_2.button("Next", key="python_next", on_click=next_code):
            pass

    # Display a text box in the second column for user input
    with col2:
        col2.subheader("Exercise")
        user_input = st.text_area("label", height=400, label_visibility="collapsed", key="python_prac")
        check, _, submit = st.columns([1, 2.7, 1])

        if check.button("Check", key="python_check"):
            if user_input:
                check_result = check_syntax(code_sections[st.session_state.section_index]["header"], user_input)
                st.write("Check Result:")
                st.code(check_result)
            else:
                st.warning("Please enter some code before checking.")
