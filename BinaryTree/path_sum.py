class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, target_sum):
    if root is None:
        return False

    # Check whether this is a leaf node
    if root.left is None and root.right is None:
        return root.val == target_sum

    remaining = target_sum - root.val

    return (
        has_path_sum(root.left, remaining)
        or has_path_sum(root.right, remaining)
    )


# Create Binary Tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

target_sum = 22

print("Has path sum?", has_path_sum(root, target_sum))
