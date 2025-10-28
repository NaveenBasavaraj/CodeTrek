# 📘 Valid Parentheses Problem

- Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

- An input string is valid if:

  * Open brackets must be closed by the same type of brackets.
  * Open brackets must be closed in the correct order.
  * Every close bracket has a corresponding open bracket of the same type.
 
-----

## 🔹 What the code does

  - Checks if a string containing brackets `()[]{}` is **valid**.
  - A valid string must meet the following criteria:
    1.  Every opening bracket has a matching closing bracket.
    2.  Brackets close in the **correct order** (e.g., `([)]` is invalid).
    3.  No unmatched brackets remain at the end.

-----

## 🔹 Step-by-step logic

1.  **Stack for memory**: Use a **stack** to store opening brackets. The stack's **Last-In, First-Out (LIFO)** behavior is a perfect match for the rule that the last bracket opened must be the first one closed.

2.  **Mapping dictionary**: Create a dictionary to map each closing bracket to its corresponding opening bracket. This allows for quick, constant-time lookups.

    ```python
    {")": "(", "}": "{", "]": "["}
    ```

3.  **Iterate through string**: Process each character in the input string.

      - If the character is an **opening bracket**, push it onto the stack.
      - If the character is a **closing bracket**, check if the stack is not empty and if the top element of the stack is the correct matching opening bracket.
          - If they match, pop the opening bracket from the stack.
          - If they don't match, or the stack is empty, the string is invalid, so return `False` immediately.

4.  **Final check**: After the loop finishes, check if the stack is empty.

      - If the stack is empty, every opening bracket was successfully closed, and the string is **valid** (`True`).
      - If the stack is not empty, there are unclosed brackets, and the string is **invalid** (`False`).

-----

## 🔹 Example Walkthroughs

**Example 1: `"()[]{}"` → ✅ Valid**

  - Push `(` → stack: `["("]`
  - See `)`. Matches `(`. Pop. → stack: `[]`
  - Push `[` → stack: `["["]`
  - See `]`. Matches `[`. Pop. → stack: `[]`
  - Push `{` → stack: `["{"]`
  - See `}`. Matches `{`. Pop. → stack: `[]`
  - End of string. Stack is empty. Return `True`.

**Example 2: `"([)]"` → ❌ Invalid**

  - Push `(` → stack: `["("]`
  - Push `[` → stack: `["(", "["]`
  - See `)`. Expected `(`, but top is `[`. **Mismatch**. Return `False`.

**Example 3: `"((("` → ❌ Invalid**

  - Push `(` → stack: `["("]`
  - Push `(` → stack: `["(", "("]`
  - Push `(` → stack: `["(", "(", "("]`
  - End of string. Stack is not empty. Return `False`.

-----

## 🔹 Data Structure / Pattern

  - The primary data structure used is a **stack (LIFO)**.
  - The underlying pattern is "Last opened must be closed first."
  - This pattern is also used in problems like:
      - **Reverse Polish Notation (RPN)** evaluation.
      - Tracking the minimum element in a stack (**MinStack**).
  - Here, the stack's purpose is to track **unclosed opening brackets**.

-----

## 🔹 Complexity

  - **Time Complexity:** $O(n)$, as we only need to iterate through the string once.
  - **Space Complexity:** $O(n)$, in the worst-case scenario (e.g., a string of all opening brackets), the stack will hold all $n$ characters.

-----

## 🔹 How to remember

  - Whenever you need to match nested pairs, a **stack** is the ideal data structure.
  - A closing bracket must always correspond to the **last opening bracket** you encountered.
  - A valid string is one where the stack is completely **empty** at the end.

-----

## 🚀 Possible Extensions

1.  **New bracket types:** Add support for additional brackets, such as `< >`.
2.  **Ignore other characters:** Adapt the logic to handle strings with non-bracket characters, like `a+(b*c)`, by simply ignoring them.
3.  **Return first error:** Instead of a simple `True`/`False` return, modify the function to return the index of the first invalid character.
4.  **HTML/XML validation:** Extend the logic to validate more complex nested structures, such as HTML tags (`<div> ... </div>`).