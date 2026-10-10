class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# First sorted list: 1 -> 3 -> 5
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

# Second sorted list: 2 -> 4 -> 6
list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged = merge_lists(list1, list2)

print("Merged list:")
print_list(merged)
