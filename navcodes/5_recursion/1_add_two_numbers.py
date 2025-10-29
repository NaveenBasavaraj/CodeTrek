class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def recursive(self, l1, l2, carry=0):
        if not l1 and not l2 and carry == 0:
            return None 
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry 

        new_node = ListNode(total%10)

        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        new_node.next = self.recursive(next_l1, next_l2, total // 10)

        return new_node

    def iterative(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy 
        carry = 0 

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            total = val1 + val2 + carry 

            carry = total // 10
            digit = total % 10
            tail.next = ListNode(digit)
            tail = tail.next

            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
        return dummy.next