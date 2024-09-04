import streamlit as st
from openai import OpenAI

def ct_cpp_columns():
    col1, col2 = st.columns(2)

    code_sections = [
        {
            "header": "Lower Bound",
            "code": '''
    int lowerBound(const vector<int>& nums, int target) {
        int left = 0, right = nums.size();

        while (left < right) {
            // Avoid potential overflow
            int mid = left + (right - left) / 2;
            if (valid(nums[mid], target)) {
                // Move the right pointer if the mid value is valid
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    bool valid(int num, int target) {
        // Check if the current number meets the target condition
        return num >= target;
    }
    ''',
        },
        {
            "header": "Trie",
            "code": '''
    class TrieNode {
    public:
        TrieNode* children[26];
        bool end;

        TrieNode() {
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
            end = false;
        }
    };

    class Trie {
    private:
        TrieNode* root;

    public:
        Trie() {
            root = new TrieNode();
        }

        void insert(const std::string& word) {
            TrieNode* node = root;
            for (char ch : word) {
                int index = ch - 'a';
                if (node->children[index] == nullptr) {
                    node->children[index] = new TrieNode();
                }
                node = node->children[index];
            }
            node->end = true;
        }

        TrieNode* searchPrefix(const std::string& prefix) {
            TrieNode* node = root;
            for (char ch : prefix) {
                int index = ch - 'a';
                if (node->children[index] == nullptr) {
                    return nullptr;
                }
                node = node->children[index];
            }
            return node;
        }

        bool search(const std::string& word) {
            TrieNode* node = searchPrefix(word);
            return node != nullptr && node->end;
        }

        bool startsWith(const std::string& prefix) {
            return searchPrefix(prefix) != nullptr;
        }
    };
    ''',
        },
        {
            "header": "Sliding Window (longest valid)",
            "code": '''
    int longestValid(const std::vector<std::string>& strings) {
        int res = 0;
        int right = 0;
        std::unordered_set<std::string> state; // Use an unordered_set to track valid strings
        for (int i = 0; i < strings.size(); i++) {
            state.insert(strings[i]);
            // While the state is not valid, remove strings from the right
            while (!isValid(state)) {
                state.erase(strings[right]);
                right++;
            }
            res = std::max(res, i - right + 1);
        }
        return res;
    }

    bool isValid(const std::unordered_set<std::string>& state) {
        // Implement your validation logic here
        // Return true if the state is valid, false otherwise
        return true;
    }
    ''',
        },
        {
            "header": "Sliding Window (shortest valid)",
            "code": '''
    int shortestValid(const std::vector<std::string>& strings) {
        int res = strings.size() + 1;
        int right = 0;
        // Use an unordered_set to track valid strings
        std::unordered_set<std::string> state;
        for (int i = 0; i < strings.size(); i++) {
            state.insert(strings[i]);
            // While the state is valid, update the result and remove from the right
            while (isValid(state)) {
                res = std::min(res, i - right + 1);
                state.erase(strings[right]);
                right++;
            }
        }
        return res == strings.size() + 1 ? -1 : res;
    }

    bool isValid(const std::unordered_set<std::string>& state) {
        // Implement your validation logic here
        // Return true if the state is valid, false otherwise
        return true;
    }
    ''',
        },
        {
            "header": "Monotone Stack (next greater)",
            "code": '''
    std::vector<int> nextGreaterElements(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> result(n, -1);
        // Monotone stack
        std::stack<int> stack;

        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[stack.top()] < nums[i]) {
                int index = stack.top();
                stack.pop();
                result[index] = nums[i];
            }
            stack.push(i);
        }

        return result;
    }
    ''',
        },
        {
            "header": "BFS",
            "code": '''
    void bfs(const std::unordered_map<std::string, std::vector<std::string>>& graph, const std::string& start) {
        std::unordered_set<std::string> visited;
        std::queue<std::pair<std::string, int>> queue;
        queue.push({start, 0});  // Enqueue the starting node with level 0

        while (!queue.empty()) {
            auto pair = queue.front();
            queue.pop();
            std::string node = pair.first;
            int level = pair.second;

            if (visited.find(node) == visited.end()) {
                // Mark the node as visited
                visited.insert(node);
                std::cout << "Node: " << node << ", Level: " << level << std::endl;  // Process the node
                // Enqueue all unvisited neighbors with the incremented level
                for (const std::string& neighbor : graph.at(node)) {
                    if (visited.find(neighbor) == visited.end()) {
                        queue.push({neighbor, level + 1});
                    }
                }
            }
        }
    }
    ''',
        },
        {
            "header": "Topological Sort",
            "code": '''
    void topologicalSort(const std::unordered_map<std::string, std::vector<std::string>>& graph) {
        std::unordered_map<std::string, int> indegree;
        // Initialize in-degrees
        for (const auto& pair : graph) {
            indegree[pair.first] = 0;
        }
        for (const auto& pair : graph) {
            for (const std::string& neighbor : pair.second) {
                indegree[neighbor]++;
            }
        }

        // Initialize the queue with nodes having 0 in-degree
        std::queue<std::string> queue;
        for (const auto& pair : indegree) {
            if (pair.second == 0) {
                queue.push(pair.first);
            }
        }

        while (!queue.empty()) {
            std::string node = queue.front();
            queue.pop();
            std::cout << node << std::endl;
            // Decrease the in-degree of neighbors
            for (const std::string& neighbor : graph.at(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.push(neighbor);
                }
            }
        }
    }
    ''',
        },
        {
            "header": "Union Find",
            "code": '''
    class UnionFind {
    private:
        std::vector<int> parent;
        std::vector<int> rank;

    public:
        UnionFind(int size) {
            parent.resize(size);
            rank.resize(size, 1);
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        int find(int p) {
            if (parent[p] != p) {
                parent[p] = find(parent[p]); // Path compression
            }
            return parent[p];
        }

        void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);

            if (rootP != rootQ) {
                // Union by rank
                if (rank[rootP] > rank[rootQ]) {
                    parent[rootQ] = rootP;
                } else if (rank[rootP] < rank[rootQ]) {
                    parent[rootP] = rootQ;
                } else {
                    parent[rootQ] = rootP;
                    rank[rootP]++;
                }
            }
        }

        bool connected(int p, int q) {
            return find(p) == find(q);
        }
    };
    ''',
        },
        {
            "header": "Rolling Hash",
            "code": '''
    class RollingHash {
    private:
        static const int BASE = 257;
        static const int MOD = 1000000007;
        long long hashValue;
        long long power;

    public:
        RollingHash() : hashValue(0), power(1) {}

        long long computeHash(const std::string& s) {
            hashValue = 0;
            power = 1;
            for (char ch : s) {
                hashValue = (hashValue * BASE + ch) % MOD;
                power = (power * BASE) % MOD;
            }
            return hashValue;
        }

        long long rollHash(char oldChar, char newChar) {
            hashValue = (hashValue * BASE - oldChar * power + newChar) % MOD;
            if (hashValue < 0) {
                hashValue += MOD;
            }
            return hashValue;
        }
    };
    ''',
        }
    ]

    # keep track of current section
    if 'section_index' not in st.session_state:
        st.session_state.section_index = 0

    if 'cppcodes' not in st.session_state:
        st.session_state.cppcodes = code_sections

    def display_code():
        st.subheader(st.session_state.cppcodes[st.session_state.section_index]["header"])
        if not hide:
            st.code(st.session_state.cppcodes[st.session_state.section_index]["code"], language="cpp")
        else:
            st.code("Code template hidden.")

    def next_code():
        if st.session_state.section_index + 1 >= len(st.session_state.cppcodes):
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

    hide = st.checkbox("Hide code", key="cpp_hide")
    # Display the current code section in the first column
    with col1:
        display_code()
        button_1, _, button_2, = st.columns([1, 2.7, 1])

        if button_1.button("Previous", key="cpp_prev", on_click=previous_code):
            pass

        if button_2.button("Next", key="cpp_next", on_click=next_code):
            pass

    # Display a text box in the second column for user input
    with col2:
        col2.subheader("Exercise")
        user_input = st.text_area("label", height=400, label_visibility="collapsed", key="cpp_prac")
        check, _, submit = st.columns([1, 2.7, 1])

        if check.button("Check", key="cpp_check"):
            if user_input:
                check_result = check_syntax(code_sections[st.session_state.section_index]["header"], user_input)
                st.write("Check Result:")
                st.code(check_result)
            else:
                st.warning("Please enter some code before checking.")
