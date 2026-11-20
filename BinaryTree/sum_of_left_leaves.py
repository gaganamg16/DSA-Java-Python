class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_left_leaves(root):
    if root is None:
        return 0

    total = 0

    # Check whether left child is a leaf
    if root.left:
        if root.left.left is None and root.left.right is None:
            total += root.left.val
        else:
            total += sum_of_left_leaves(root.left)

    # Visit right subtree
    total += sum_of_left_leaves(root.right)

    return total


# Create Binary Tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Sum of Left Leaves:", sum_of_left_leaves(root))
