
---

## 📒 @notes for `evalRPN`

Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include '+', '-', '*', and '/'.
- Assume that division between integers always truncates toward zero.

```
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

```

### 🔹 What the code does

* Evaluates an expression written in **Reverse Polish Notation (RPN)**, also called **postfix expression**.
* Instead of normal math `"3 + 4"`, RPN writes it as `"3 4 +"`.

---

### 🔹 Step-by-step logic

1. **Use a stack** to keep numbers.
2. **Loop over tokens** (each number or operator).
3. If the token is a **number** → push it into the stack.
4. If the token is an **operator** (`+, -, *, /`) →

   * Pop the **last two numbers** from the stack → let’s call them `a` (last popped) and `b` (second last popped).
   * Perform the operation in **order**:

     * `b + a`
     * `b - a` (NOT `a - b`)
     * `b * a`
     * `b / a` (truncate toward 0).
   * Push the result back into the stack.
5. At the end, the stack will have only **one number**, which is the final result.

---

### 🔹 Why `b - a` and not `a - b`?

* Because in RPN, the operator applies to the **two most recent numbers in order**:

  * Example: `["5","3","-"]`

    * Stack after `5,3` → `[5,3]`
    * When `-` comes → pop `a=3`, `b=5`
    * Correct operation is `5 - 3 = 2`.
    * If we did `a - b = 3 - 5`, we’d get the wrong result.
* **Rule:** Second last popped = left operand, last popped = right operand.

---

### 🔹 Data Structure / Pattern

* **Stack** (LIFO) → ideal because we need to work backward on operands.
* **Postfix expression evaluation** → classic stack-based problem.

---

### 🔹 Similar problems you’ve seen

* **Min Stack problem (Problem 17)** → there also, we pushed/popped and carefully tracked order.
* **Valid Parentheses problem** → stack was used to manage structure/order.
* RPN is basically another application of **stack order control**.

---

### 🔹 How to remember

* "When you see postfix (RPN) → **use a stack**."
* "Pop twice: first = right operand, second = left operand."
* "Push the result back, continue till end."

---

