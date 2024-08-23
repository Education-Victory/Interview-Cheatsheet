import streamlit as st

def ct_java_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Lower Bound')
        col1.code('''
// Finds the index of the first element in a sorted list that is
// greater than or equal to a specified target value using binary search.
public static int lowerBound(int[] nums, int target) {
    int left = 0, right = nums.length;

    while (left < right) {
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

public static boolean valid(int num, int target) {
    // Check if the current number meets the target condition
    return num >= target;
}
''', language="java")

        col1.subheader('Trie')
        col1.code('''
class Trie {
    Trie[] children;
    boolean end;

    public Trie() {
        children = new Trie[26];
        end = false;
    }
    public void insert(String word) {
        Trie node = this;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';
            // Create a new Trie node if it doesn't exist for the character
            if (node.children[index] == null) {
                node.children[index] = new Trie();
            }
            node = node.children[index];
        }
        node.end = true;
    }

    public boolean search(String word) {
        Trie node = this;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';
            // Check if the character path exists and if it's the end of a word
            if (node.children[index] == null || !node.children[index].end) {
                return false;
            }
            node = node.children[index];
        }
        return node != null && node.end;
    }
}
''', language="java")

        col1.subheader('Sliding Window (longest valid)')
        col1.code('''
public static int longestValid(String[] strings) {
    int res = 0;
    int right = 0;
    // Use a HashSet to track valid strings
    HashSet<String> state = new HashSet<>();
    for (int i = 0; i < strings.length; i++) {
        state.add(strings[i]);
        // While the state is not valid, remove strings from the right
        while (!isValid(state)) {
            state.remove(strings[right]);
            right++;
        }
        res = Math.max(res, i - right + 1);
    }
    return res;
}

private static boolean isValid(HashSet<String> state) {
    // Implement your validation logic here
    // Return true if the state is valid, false otherwise
    return true;
}
''', language="java")

        col1.subheader('Sliding Window (shortest valid)')
        col1.code('''
public static int shortestValid(String[] strings) {
    int res = strings.length + 1;
    int right = 0;
    // Use a HashSet to track valid strings
    HashSet<String> state = new HashSet<>();
    for (int i = 0; i < strings.length; i++) {
        state.add(strings[i]);
        // While the state is valid, update the result and remove from the right
        while (isValid(state)) {
            res = Math.min(res, i - right + 1);
            state.remove(strings[right]);
            right++;
        }
    }
    return res == strings.length + 1 ? -1 : res;
}

private static boolean isValid(HashSet<String> state) {
    // Implement your validation logic here
    // Return true if the state is valid, false otherwise
    return true;
}
''', language="java")

        col1.subheader('Monotone Stack (next greater)')
        col1.code('''
public static int[] nextGreaterElements(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    Arrays.fill(result, -1);
    Stack<Integer> stack = new Stack<>();  // Monotone stack

    for (int i = 0; i < n; i++) {
        while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
            int index = stack.pop();
            result[index] = nums[i];
        }
        stack.push(i);
    }

    return result;
}
''', language="java")

        col1.subheader('BFS')
        col1.code('''
public static Void bfs(Map<String, List<String>> graph, String start) {
    Set<String> visited = new HashSet<>();
    Queue<Pair<String, Integer>> queue = new LinkedList<>();
    queue.add(new Pair<>(start, 0));  // Enqueue the starting node with level 0

    while (!queue.isEmpty()) {
        Pair<String, Integer> pair = queue.poll();
        String node = pair.getKey();
        int level = pair.getValue();

        if (!visited.contains(node)) {
            // Mark the node as visited
            visited.add(node);
            System.out.println("Node: " + node + ", Level: " + level);
            // Enqueue all unvisited neighbors with the incremented level
            for (String neighbor : graph.get(node)) {
                if (!visited.contains(neighbor)) {
                    queue.add(new Pair<>(neighbor, level + 1));
                }
            }
        }
    }
}
''', language="java")

        col1.subheader('Topological Sort')
        col1.code('''
void topologicalSort(Map<String, List<String>> graph) {
    Map<String, Integer> indegree = new HashMap<>();  // Track the in-degrees of nodes
    for (String node : graph.keySet()) {
        indegree.put(node, 0);
    }
    for (String node : graph.keySet()) {
        for (String neighbor : graph.get(node)) {
            indegree.put(neighbor, indegree.get(neighbor) + 1);
        }
    }

    // Initialize the queue with nodes having 0 in-degree
    Queue<String> queue = new LinkedList<>();
    for (String node : indegree.keySet()) {
        if (indegree.get(node) == 0) {
            queue.add(node);
        }
    }

    while (!queue.isEmpty()) {
        String node = queue.poll();
        System.out.println(node);
        // Decrease the in-degree of neighbors
        for (String neighbor : graph.get(node)) {
            indegree.put(neighbor, indegree.get(neighbor) - 1);
            if (indegree.get(neighbor) == 0) {
                queue.add(neighbor);
            }
        }
    }
}
''', language="java")
