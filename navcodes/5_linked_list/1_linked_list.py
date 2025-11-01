from treenode import TreeNode

class LinkedList:
    def __init__(self):
        self.head = TreeNode(-1)
        self.tail = self.head
        self.size = 0
    
    def append(self, val):
        self.tail.next = TreeNode(val)
        self.tail = self.tail.next
        self.size += 1
        return self.tail

    def prepend(self, val):
        new_node = TreeNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
        return self.head

    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty list")

        prev = self.head
        curr = self.head.next

        while curr.next:
            prev = curr
            curr = curr.next

        # curr is last node, prev is node before it
        prev.next = None
        self.tail = prev
        self.size -= 1
        return curr.val

    def pop_first(self):
        if self.size == 0:
            raise IndexError("pop from empty list")
        first = self.head.next
        self.head.next = first.next
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
        return first.val

    def reverse(self):
        prev = None
        curr = self.head.next
        self.tail = curr  # after reverse, the original head becomes tail
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        self.head.next = prev  # connect dummy head to new first node

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print("None")

    
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.print()         # 1 -> 2 -> 3 -> None
    ll.prepend(0)
    ll.print()         # 0 -> 1 -> 2 -> 3 -> None
    print(ll.pop())    # 3
    print(ll.pop_first())  # 0
    ll.reverse()
    ll.print()         # 2 -> 1 -> None