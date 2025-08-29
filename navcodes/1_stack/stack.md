# 📘 Stack Implementation Notes

## What is a Stack?
- A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.  
- Think of it like a **stack of plates**:  
  - **Push** → add a plate on top.  
  - **Pop** → remove the plate from the top.  
  - **Top** → see the plate on the top without removing it.

---

## Methods Implemented

### `__init__`
- Initializes the stack as an empty list.
- Maintains `top` for quick access to the last element.

### `push(val)`
- Adds an element to the stack.
- Updates `top` to the new element.

### `pop()`
- Removes and returns the **last inserted element**.
- Updates `top` to the new last element (or `None` if stack is empty).
- Handles the **empty stack case** safely.

---

## Example Walkthrough
```python
s = Stack()
s.push(5)     # stack = [5], top = 5
s.push(10)    # stack = [5, 10], top = 10
s.push(15)    # stack = [5, 10, 15], top = 15

s.pop()       # removes 15 → stack = [5, 10], top = 10
s.pop()       # removes 10 → stack = [5], top = 5
s.pop()       # removes 5 → stack = [], top = None
s.pop()       # empty → "Stack is empty, cannot pop."
