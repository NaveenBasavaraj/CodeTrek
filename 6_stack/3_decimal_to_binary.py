class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        if not self.stack:
            return True
        return False
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop() # item on the top

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

class DecimalBinaryConversion:
    def toBinary(self, decimal_number):
        rem_stack = Stack()
        binstring = ""

        while decimal_number > 0:
            rem = decimal_number % 2
            rem_stack.push(rem)
            decimal_number = decimal_number//2
        
        while not rem_stack.is_empty():
            binstring = binstring + str(rem_stack.pop())
        return binstring

if __name__ == "__main__":
    s = DecimalBinaryConversion()
    print(s.toBinary(233))

