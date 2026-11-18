class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return (
            validate(node.left, low, node.val)
            and validate(node.right, node.val, high)
        )

    return validate(root, float("-inf"), float("inf"))


# Create a Binary Search Tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print("Is valid BST?", is_valid_bst(root))
