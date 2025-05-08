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

s = Stack()
s.push(10)
s.push(20)
s.pop()

print(s.peek())
print(s.is_empty())
