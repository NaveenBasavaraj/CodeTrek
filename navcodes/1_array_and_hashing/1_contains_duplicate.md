
---

# 📘 @notes: Contains Duplicate Problem

---

## 🔹 What the code does

* Checks if a list contains **any repeated elements**.
* Returns `True` if a duplicate exists, otherwise `False`.

---

## 🔹 Step-by-step logic (Solution 1: `seen` set)

1. **Use a set as memory**

   * Set stores all elements seen so far.
   * Rule: Sets have **O(1) membership checks** → fast lookup.

2. **Iterate through list**

   * For each number:

     * If it’s already in `seen` → **duplicate found** → return `True` immediately.
     * Else → add it to `seen` and continue.

3. **End of iteration**

   * If no duplicates found → return `False`.

---

## 🔹 Step-by-step logic (Solution 2: `len(set(nums))`)

1. Convert list to a set → removes duplicates automatically.
2. Compare lengths:

   * `len(set(nums)) < len(nums)` → duplicates exist.
   * Else → all elements unique → no duplicates.

---

## 🔹 Data Structure / Pattern

* **Pattern:** "Use a set to track already seen items for duplicate detection."

* **When to use:**

  * Need **fast membership check**.
  * Can short-circuit when duplicate found (Solution 1).
  * Simple one-liner if scanning full list is acceptable (Solution 2).

* **Related problems:**

  * MinStack (tracking min using auxiliary stack/set)
  * RPN evaluation (stack to track operands)
  * Any problem where **history or uniqueness matters** → sets or hashmaps are handy.

---

## 🔹 Complexity

| Solution         | Time Complexity | Space Complexity | Notes                          |
| ---------------- | --------------- | ---------------- | ------------------------------ |
| `seen` set       | O(n) average    | O(n)             | Stops early if duplicate found |
| `len(set(nums))` | O(n)            | O(n)             | Always processes entire list   |

---

## 🔹 How to remember

* "Whenever you need to check for **duplicates** → think **set/hashmap**."
* "Solution 1 → efficient for early duplicates."
* "Solution 2 → concise one-liner, but always scans the whole list."

---


