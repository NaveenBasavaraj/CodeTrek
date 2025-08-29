# MinStack Implementation - Notes

## Code Overview

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, val:int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]
```

---

## Key Concepts

1. **Two Stacks**  
   - `self.stack`: Stores all pushed values normally.  
   - `self.minstack`: Keeps track of the minimum value at each push.

2. **Push Operation**  
   - Add element to `stack`.  
   - Compute the minimum between the new value and the last minimum.  
   - Push this minimum into `minstack`.

3. **Pop Operation**  
   - Remove top element from both `stack` and `minstack`.  
   - Ensures both stacks remain aligned.

4. **Top Operation**  
   - Returns the top element of `stack`.  

5. **GetMin Operation**  
   - Returns the top element of `minstack`, which represents the current minimum.  

---

## Example Walkthrough

### Push Sequence: `push(5), push(3), push(7), push(2)`

- After `push(5)` → `stack = [5]`, `minstack = [5]`  
- After `push(3)` → `stack = [5, 3]`, `minstack = [5, 3]`  
- After `push(7)` → `stack = [5, 3, 7]`, `minstack = [5, 3, 3]`  
- After `push(2)` → `stack = [5, 3, 7, 2]`, `minstack = [5, 3, 3, 2]`  

### GetMin
- `getMin()` → `2`

### Pop
- `pop()` removes `2` → `stack = [5, 3, 7]`, `minstack = [5, 3, 3]`  
- Now `getMin()` → `3`  

---

## Time & Space Complexity

- **Push**: `O(1)`  
- **Pop**: `O(1)`  
- **Top**: `O(1)`  
- **GetMin**: `O(1)`  
- **Space Complexity**: `O(n)` (since we maintain two stacks)

---

## Advantages
- Constant-time retrieval of minimum value.  
- Simple implementation using two stacks.

## Limitations
- Uses extra space for maintaining `minstack`.  
- Not memory-optimal when the stack is very large.
