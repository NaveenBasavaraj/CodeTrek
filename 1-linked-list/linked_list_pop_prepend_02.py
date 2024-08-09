from linked_list_01 import LinkedList, ListNode

class LinkedList(LinkedList):
    def prepend(self, val):
        newnode = ListNode(val)
        if self.length == 0:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1
        return True
    
    def pop_first(self):
        if not self.length:
            return None
        currhead = self.head
        self.head = self.head.next
        currhead.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return currhead

if __name__ == "__main__":
    my_linked_list = LinkedList(10)
    print('LL before prepend():')
    
    my_linked_list.print_list()
    my_linked_list.prepend(9)
    my_linked_list.prepend(8)
    my_linked_list.prepend(7)
    my_linked_list.prepend(6)
    my_linked_list.prepend(5)
    my_linked_list.prepend(4)
    print('LL after preppend():')
    
    my_linked_list.print_list()

    print('\nLL after pop():')
    my_linked_list.pop_first()

    my_linked_list.print_list()