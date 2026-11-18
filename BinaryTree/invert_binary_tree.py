class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


# Create Binary Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


def print_tree(root):
    if root is None:
        return

    print(root.val, end=" ")
    print_tree(root.left)
    print_tree(root.right)


print("Before Inverting:")
print_tree(root)

invert_tree(root)

print("\nAfter Inverting:")
print_tree(root)
