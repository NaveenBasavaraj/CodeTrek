
---

## 📒 @notes for `MinStack`


Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
```
Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
```
### 🔹 What the code does

* Implements a **special stack** that can return the **minimum element** in constant time.
* Normal stack operations (`push`, `pop`, `top`) work as usual, but it adds `getMin` that always gives the smallest element quickly.

---

### 🔹 Step-by-step logic

1. **Two Stacks are used**

   * `stack`: keeps all values.
   * `minstack`: keeps track of the running minimum (minimum value *at each point in time*).

2. **Push**

   * Push value into `stack`.
   * Push the smaller one between `val` and the previous min into `minstack`.
   * So `minstack[-1]` always represents the min so far.

3. **Pop**

   * Pop from both `stack` and `minstack` so they stay aligned.

4. **Top**

   * Just return the top of `stack`.

5. **GetMin**

   * Return the top of `minstack` → guaranteed to be the current minimum.

---

### 🔹 Why do we need two stacks?

* If we used only one stack, we’d need to **scan the whole stack** to find the min each time → `O(n)`.
* With a parallel `minstack`, we always know the current min instantly → `O(1)`.

---

### 🔹 Example Run

Sequence: `push(5), push(3), push(7), push(2)`

* `stack = [5]`, `minstack = [5]`
* `stack = [5,3]`, `minstack = [5,3]`
* `stack = [5,3,7]`, `minstack = [5,3,3]`
* `stack = [5,3,7,2]`, `minstack = [5,3,3,2]`
* `getMin()` → `2`
* After `pop()` → `stack = [5,3,7]`, `minstack = [5,3,3]`, so `getMin()` = `3`

---

### 🔹 Data Structure / Pattern

* **Stack** + auxiliary **min stack**.
* **Pattern**: Maintain extra structure to store "history" of key property (here, minimum).
* This is a **design trick**: parallel stacks or queues are often used when one structure alone can’t track needed properties in constant time.

---

### 🔹 Similar problems you’ve seen

* In **RPN evaluation**, we also used a stack but for arithmetic.
* Here, same idea → use stack to keep **history** of elements.
* Think of it like:

  * *RPN*: stack tracks **operands** for math.
  * *MinStack*: stack tracks **minimum values**.

---

### 🔹 Complexity

* Push, Pop, Top, GetMin → `O(1)` each.
* Space → `O(n)` because of the extra `minstack`.

---

### 🔹 How to remember

* "Whenever you need constant-time tracking of some property (like min/max), **keep a helper stack** in sync with the main one."
* "Main stack = actual values, helper stack = property snapshot."

---

