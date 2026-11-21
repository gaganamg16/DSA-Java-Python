class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root):
    if root is None:
        return 0

    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)

    return 1 + left_count + right_count


# Create a Complete Binary Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print("Total Number of Nodes:", count_nodes(root))
