class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    if val < root.val:
        return search_bst(root.left, val)

    return search_bst(root.right, val)


# Create Binary Search Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

target = 2

result = search_bst(root, target)

if result:
    print("Found:", result.val)
else:
    print("Value not found")
