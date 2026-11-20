class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if root is None:
        return 0

    # If left child is missing, go right
    if root.left is None:
        return 1 + min_depth(root.right)

    # If right child is missing, go left
    if root.right is None:
        return 1 + min_depth(root.left)

    return 1 + min(
        min_depth(root.left),
        min_depth(root.right)
    )


# Create Binary Tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Minimum Depth:", min_depth(root))
