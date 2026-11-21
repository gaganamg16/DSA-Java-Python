class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)

    elif val > root.val:
        root.right = insert_into_bst(root.right, val)

    return root


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# Create Binary Search Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print("Before Insertion:")
inorder(root)

# Insert new value
root = insert_into_bst(root, 5)

print("\nAfter Insertion:")
inorder(root)
