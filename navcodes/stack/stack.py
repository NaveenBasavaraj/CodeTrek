class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
    
    def push(self, val):
        self.stack.append(val)
        self.top = self.stack[-1]  # update top reference

    def pop(self):
        if not self.stack:  # handle empty stack safely
            print("Stack is empty, cannot pop.")
            return None
        popped_val = self.stack.pop()
        self.top = self.stack[-1] if self.stack else None  # update top after popping
        return popped_val


def main():
    s = Stack()
    
    # Push operations
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack after pushing 10, 20, 30:", s.stack)
    print("Top element:", s.top)

    # Pop operations
    print("Popped:", s.pop())
    print("Stack after pop:", s.stack)
    print("Top element:", s.top)

    # Popping all elements
    s.pop()
    s.pop()
    print("Stack after popping all:", s.stack)
    print("Top element:", s.top)

    # Try popping from empty stack
    s.pop()

if __name__ == "__main__":
    main()
