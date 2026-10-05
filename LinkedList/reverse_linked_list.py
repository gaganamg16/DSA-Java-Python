class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


# Create linked list: 1 -> 2 -> 3 -> 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed list
current = head

while current:
    print(current.data, end=" ")
    current = current.next