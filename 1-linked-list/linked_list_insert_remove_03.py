from linked_list_01 import LinkedList, ListNode

class LinkedList(LinkedList):
    def get_node(self, node_index):
        if node_index >= self.length:
            return None
        if node_index <= 0:
            return None
        currnode = self.head
        for _ in range(node_index):
            currnode = currnode.next
        return currnode
    
    def set_value_to_node(self, node_index, val):
        currnode = self.get_node(node_index)
        if currnode:
            currnode.value = val
            return True
        return False
    
    def insert(self, node_index, val):
        pass
