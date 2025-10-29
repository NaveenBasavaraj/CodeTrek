# 🎯 Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.  

You may assume that each input has exactly one solution, and you may not use the same element twice.

---

## ✅ Code Implementation (Hash Map Method)

```python
class Solution:
    def two_sum(self, nums, target):
        diff_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_dict:
                return (i, diff_dict[diff])
            else:
                diff_dict[num] = i

if __name__ == "__main__":
    s = Solution()
    print(s.two_sum([2, 7, 11, 15], 9))   # → (1, 0)
    print(s.two_sum([3, 2, 4], 6))        # → (2, 1)
    print(s.two_sum([3, 3], 6))           # → (1, 0)
```

---

## 🔍 Step-by-Step Explanation

1. **Dictionary for Fast Lookup**
   - We keep a dictionary `diff_dict` that maps **number → index**.
   - While iterating, we check if the complement (target - current number) already exists in the dictionary.

2. **Iteration**
   - For each number `num` at index `i`:
     - Compute `diff = target - num`
     - If `diff` is already in dictionary → solution found.
     - Otherwise, store current `num` with its index in dictionary.

3. **Return**
   - Return the pair of indices `(i, diff_dict[diff])`.

---

## ✨ Example Walkthroughs

### Example 1: `nums = [2, 7, 11, 15], target = 9`
- i=0 → num=2, diff=7 → not in dict → store `{2:0}`
- i=1 → num=7, diff=2 → found in dict → return (1,0) ✅

### Example 2: `nums = [3, 2, 4], target = 6`
- i=0 → num=3, diff=3 → not in dict → store `{3:0}`
- i=1 → num=2, diff=4 → not in dict → store `{3:0, 2:1}`
- i=2 → num=4, diff=2 → found in dict → return (2,1) ✅

### Example 3: `nums = [3, 3], target = 6`
- i=0 → num=3, diff=3 → not in dict → store `{3:0}`
- i=1 → num=3, diff=3 → found in dict → return (1,0) ✅

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n)` → One pass through the list.
- **Space Complexity:** `O(n)` → Dictionary stores up to `n` elements.

---

## 🛠️ Alternative Solutions

1. **Brute Force**
   - Check all pairs → `O(n²)`
   - Not efficient for large arrays.

2. **Sorting + Two Pointers**
   - Sort array + use two pointers → `O(n log n)` (due to sorting).
   - Problem: indices are lost after sorting, so you’d need extra mapping.

3. **Hash Map (this method)**
   - Most efficient and clean → `O(n)` time, `O(n)` space.
   - ✅ Best method for interviews.

---

## 📌 Key Takeaways
- Always think of **hash maps/dictionaries** when you need **fast lookups**.
- `Brute Force` is simplest but inefficient.
- `Two Pointers` works only when array is sorted (not suitable here).
- `Hash Map` is the optimal solution most interviewers expect.
