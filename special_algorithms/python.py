import streamlit as st

def sa_python_columns():
    col1, col2 = st.columns(2)

    with col1:
        col1.subheader('Morris Traversal')
        col1.code('''
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

