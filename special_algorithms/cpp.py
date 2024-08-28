import streamlit as st

def sa_cpp_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Morris Traversal')
        col1.code('''
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

