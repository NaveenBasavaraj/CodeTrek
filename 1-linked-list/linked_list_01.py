class ListNode:
    def __init__(self, value=None, next=None):
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
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, val):
        newnode = ListNode(val)
        if not self.length:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        return True
    
    def pop(self):
        if not self.length:
            return None
        currnode = self.head
        while currnode.next:
            previous_node = currnode
            currnode = currnode.next
        self.tail = previous_node
        self.tail.next = None
        self.length -= 1
        if not self.length:
            self.head = self.tail = None
        return currnode

        

if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    print('LL before append():')
    
    my_linked_list.print_list()
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    print('LL after append():')
    
    my_linked_list.print_list()

    print('\nLL after pop():')
    my_linked_list.pop()

    my_linked_list.print_list()
