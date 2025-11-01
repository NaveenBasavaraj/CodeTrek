from treenode import TreeNode

def reverse(head):
    if not head:
        return None
    newhead = head
    if head.next:
        newhead = reverse(head.next)
        head.next.next = head
    head.next = None
    return newhead

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == '__main__':
    # Create linked list: 1 -> 2 -> 3 -> None
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.next = b
    b.next = c

    print("Original List:")
    print_list(a)

    # Reverse the linked list
    new_head = reverse(a)

    print("\nReversed List:")
    print_list(new_head)