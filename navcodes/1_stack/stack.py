class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()