

````markdown
# 📘 @notes: Valid Parentheses Problem

---

## 🔹 What the code does
- Checks if a string with brackets `()[]{}` is **valid**.  
- A valid string means:
  1. Every opening bracket has a matching closing bracket.
  2. Brackets close in the **correct order** (no crossing like `([)]`).
  3. No unmatched brackets remain at the end.  

---

## 🔹 Step-by-step logic
1. **Stack for memory**
   - Use a stack to store opening brackets.
   - Rule of thumb: *Last opened must be the first closed* → LIFO → stack.

2. **Mapping dictionary**
   - Closing → Opening map for quick checking:
     ```python
     {")": "(", "}": "{", "]": "["}
     ```
   - This lets us instantly know what opening we expect.

3. **Iterating through string**
   - If char is **opening** → push to stack.
   - If char is **closing**:
     - Check stack is not empty AND top matches.
     - If matches → pop.
     - If not → return `False` immediately.

4. **Final check**
   - If stack is empty at the end → valid.
   - If stack has leftovers → invalid.

---

## 🔹 Example Walkthroughs
**Example 1:** `"()[]{}"` → ✅ Valid  
- Push `(` → stack = ["("]  
- See `)` → matches `(` → pop → []  
- Push `[` → ["["]  
- See `]` → matches `[` → pop → []  
- Push `{` → ["{"]  
- See `}` → matches `{` → pop → []  
- End with empty stack → True  

**Example 2:** `"([)]"` → ❌ Invalid  
- Push `(` → ["("]  
- Push `[` → ["(", "["]  
- See `)` → expected `(` but top is `[` → mismatch → False  

**Example 3:** `"((("` → ❌ Invalid  
- Push three times → ["(", "(", "("]  
- End with non-empty stack → False  

---

## 🔹 Data Structure / Pattern
- **Stack (LIFO)** is the core tool.  
- **Pattern:** "Last opened must be closed first."  
- Same family as:  
  - MinStack (stack to track min).  
  - RPN Evaluation (stack to track operands).  
  - Here: stack tracks *unclosed brackets*.  

---

## 🔹 Complexity
- Time → `O(n)` (scan string once).  
- Space → `O(n)` (worst case: all openings).  

---

## 🔹 How to remember
- "Whenever you need to match pairs with nesting → **use a stack**."  
- "Closing bracket? → must match the last opening bracket."  
- "Valid string = stack empty at the end."  

---

## 🚀 Possible Extensions
1. Add `< >` as valid brackets.  
2. Ignore non-bracket characters (`a+(b*c)`).  
3. Return **index of first error** instead of just False.  
4. Extend logic to **HTML/XML tag validation** (like `<div> ... </div>`).  

````

---
