class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    inorder_index = {
        value: index for index, value in enumerate(inorder)
    }

    preorder_index = 0

    def construct(left, right):
        nonlocal preorder_index

        if left > right:
            return None

        # First element in preorder is the root
        root_value = preorder[preorder_index]
        preorder_index += 1

        root = TreeNode(root_value)

        # Find root position in inorder
        mid = inorder_index[root_value]

        # Construct left and right subtrees
        root.left = construct(left, mid - 1)
        root.right = construct(mid + 1, right)

        return root

    return construct(0, len(inorder) - 1)


def print_postorder(root):
    if root is None:
        return

    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val, end=" ")


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree(preorder, inorder)

print("Postorder Traversal:", end=" ")
print_postorder(root)
