import streamlit as st

def sa_java_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Morris Traversal')
        col1.code('''
// Leetcode 94: Binary Tree Inorder Traversal
class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int x) {
        val = x;
        left = right = null;
    }
}

public class InorderTraversal {
    public static void morrisTraversal(TreeNode root) {
        TreeNode current = root;

        while (current != null) {
            if (current.left == null) {
                System.out.print(current.val + " ");
                current = current.right;
            } else {
                // Find the inorder predecessor of current
                TreeNode predecessor = current.left;
                while (predecessor.right != null && predecessor.right != current) {
                    predecessor = predecessor.right;
                }

                // Make current as right child of its predecessor
                if (predecessor.right == null) {
                    predecessor.right = current;
                    current = current.left;
                } else {
                    // Revert the changes made to restore the original tree
                    predecessor.right = null;
                    System.out.print(current.val + " ");
                    current = current.right;
                }
            }
        }
    }

    public static void main(String[] args) {
        // Constructing a simple binary tree
        //       1
        //      / \\
        //     2   3
        //    / \\
        //   4   5
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        morrisTraversal(root);  // Output: 4 2 5 1 3
    }
}
''', language="java")

        col1.subheader('Floyd\'s Cycle Detection Algorithm')
        col1.code('''
// Leetcode 141: Linked List Cycle
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class FloydCycleDetection {
    public static boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode tortoise = head;
        ListNode hare = head;

        while (hare != null && hare.next != null) {
            // Move tortoise by 1
            tortoise = tortoise.next;
            // Move hare by 2
            hare = hare.next.next;
            // Cycle detected
            if (tortoise == hare) {
                return true;
            }
        }
        // No cycle
        return false;
    }

    public static void main(String[] args) {
        // Creating a linked list with a cycle
        // 1 -> 2 -> 3 -> 4
        //      ^         |
        //      |_________|
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        // Creating a cycle
        head.next.next.next.next = head.next;
        // Output: true
        System.out.println(hasCycle(head));
    }
}
''', language="java")

        col1.subheader('Boyer–Moore majority vote algorithm')
        col1.code('''
// Leetcode 169: Majority Element
public class BoyerMooreMajorityVote {
    public static Integer boyerMooreMajorityVote(int[] nums) {
        Integer candidate = null;
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

        return count > nums.length / 2 ? candidate : null;
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 3};
        // Output: 3
        System.out.println(boyerMooreMajorityVote(nums));
    }
}
''', language="java")

        col1.subheader('Reversal algorithm for array rotation')
        col1.code('''
// Leetcode 189: Rotate Array
public class ArrayRotation {
    // Function to reverse a portion of the array
    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    // Function to rotate the array
    public static void rotate(int[] arr, int d) {
        int n = arr.length;
        d = d % n;  // Handle cases where d >= n
        reverse(arr, 0, d - 1);   // Step 1: Reverse the first d elements
        reverse(arr, d, n - 1);   // Step 2: Reverse the remaining elements
        reverse(arr, 0, n - 1);   // Step 3: Reverse the entire array
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int d = 3;
        rotate(arr, d);
        for (int num : arr) {
            // Output: 4 5 6 7 1 2 3
            System.out.print(num + " ");
        }
    }
}
''', language="java")

        col1.subheader('Fast Power Algorithm')
        col1.code('''
// Leetcode 50: Pow(x, n)
public class FastPower {
    public static double fastPower(double x, int n) {
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

    public static void main(String[] args) {
        double x = 2.0;
        int n = 10;
        System.out.println(fastPower(x, n));  // Output: 1024.0
    }
}
''', language="java")

        col1.subheader('Quick Select Algorithm')
        col1.code('''
// Leetcode 215: Kth Largest Element in an Array
import java.util.Random;

public class QuickSelect {
    private static int partition(int[] arr, int left, int right, int pivotIndex) {
        int pivotValue = arr[pivotIndex];
        // Move pivot to end
        swap(arr, pivotIndex, right);
        int storeIndex = left;

        for (int i = left; i < right; i++) {
            if (arr[i] < pivotValue) {
                swap(arr, storeIndex, i);
                storeIndex++;
            }
        }

        // Move pivot to its final place
        swap(arr, storeIndex, right);
        return storeIndex;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static int quickSelect(int[] arr, int left, int right, int k) {
        if (left == right) {  // Base case: only one element
            return arr[left];
        }

        Random random = new Random();
        int pivotIndex = left + random.nextInt(right - left + 1);
        pivotIndex = partition(arr, left, right, pivotIndex);

        if (k == pivotIndex) {
            return arr[k];
        } else if (k < pivotIndex) {
            return quickSelect(arr, left, pivotIndex - 1, k);
        } else {
            return quickSelect(arr, pivotIndex + 1, right, k);
        }
    }

    public static void main(String[] args) {
        int[] arr = {3, 2, 1, 5, 4};
        int k = 2;  // Looking for the 3rd smallest element (index 2)
        int result = quickSelect(arr, 0, arr.length - 1, k);
        System.out.println(result);  // Output: 3
    }
}
''', language="java")

        col1.subheader('Count Primes Algorithm')
        col1.code('''
// Leetcode 204: Count Primes
public class CountPrimes {
    public static int countPrimes(int n) {
        if (n <= 2) {
            return 0;  // There are no prime numbers less than 2
        }

        boolean[] primes = new boolean[n]; // Initialize a boolean array
        for (int i = 2; i < n; i++) {
            primes[i] = true; // Initialize all entries as true
        }

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
        for (int i = 2; i < n; i++) {
            if (primes[i]) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int n = 30;
        System.out.println(countPrimes(n));  // Output: 10
    }
}
''', language="java")

