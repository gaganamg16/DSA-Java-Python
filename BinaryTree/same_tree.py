class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # Both trees are empty
    if p is None and q is None:
        return True

    # One tree is empty or values are different
    if p is None or q is None or p.val != q.val:
        return False

    # Compare left and right subtrees
    return (
        is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )


# First Binary Tree
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Second Binary Tree
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print("Are the trees same?", is_same_tree(p, q))
