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

# s = Stack()
# s.push(10)
# s.push(20)
# s.pop()

# print(s.peek())
# print(s.is_empty())

def simple_balanced_equation(equation):
    s = Stack()
    balanced = True
    i = 0
    while i < len(equation) and balanced:
        curr_symbol = equation[i]
        if curr_symbol not in "([{)]}":
            i = i+1
            continue
        if curr_symbol in "([{":
            s.push(equation[i])
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, curr_symbol):
                    balanced = False
        i = i+1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

if __name__ == "__main__":
    print(simple_balanced_equation("(2+3+(4*2+(7*3+(2*2)+5+3)))"))




