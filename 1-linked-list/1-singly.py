class ListNode:
    def __init__(self, value=value):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while curr is not None:
            print(temp.value)
            temp = temp.next
