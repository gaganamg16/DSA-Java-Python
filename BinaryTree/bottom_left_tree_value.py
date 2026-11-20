from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_bottom_left_value(root):
    if root is None:
        return None

    queue = deque([root])
    bottom_left = root.val

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # First node of each level
            if i == 0:
                bottom_left = node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return bottom_left


# Create Binary Tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print("Bottom Left Value:", find_bottom_left_value(root))
