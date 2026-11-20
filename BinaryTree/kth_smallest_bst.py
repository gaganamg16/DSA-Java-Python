class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    values = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)

    return values[k - 1]


# Create Binary Search Tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

k = 3

print("Kth Smallest Element:", kth_smallest(root, k))
