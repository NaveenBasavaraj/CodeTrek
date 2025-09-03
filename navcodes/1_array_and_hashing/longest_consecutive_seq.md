### /codemd

# Longest Consecutive Sequence — Notes

## Problem Understanding

We are asked to find the length of the **longest consecutive elements sequence** in an unsorted array.

* Consecutive means numbers that follow each other with difference of `1`.
* Example:

  * Input: `[100, 4, 200, 1, 3, 2]`
  * Output: `4` (sequence = `[1,2,3,4]`).

This is a **hashing + sequence detection** problem.

---

## Approaches

### 1. **Brute Force**

* For each number, extend streak forward until sequence breaks.
* Uses a set to check membership.

```python
for num in nums:
    streak, curr = 0, num
    while curr in store:
        streak += 1
        curr += 1
    res = max(res, streak)
```

* **Time Complexity**: Worst case `O(N^2)` (e.g., `[1,2,3,4,...,N]`).
* **Space Complexity**: `O(N)` for the set.

❌ Very slow on large inputs.

---

### 2. **Hash Set Optimized (Best Practical Approach)**

* Idea: Only start counting when `num-1` is not in the set → ensures you only start at sequence beginnings.
* Extends forward until sequence breaks.

```python
for num in numSet:
    if (num - 1) not in numSet:
        length = 1
        while (num + length) in numSet:
            length += 1
        longest = max(length, longest)
```

* **Time Complexity**: `O(N)` (each number checked at most twice).
* **Space Complexity**: `O(N)` for the set.

✅ Most widely used solution.
✅ Very clean and efficient.

---

### 3. **Hash Map (Union-Find Style)**

* Maintain a dictionary mapping number → length of sequence it belongs to.
* For each new number:

  * Length = left sequence length + right sequence length + 1.
  * Update boundaries so sequence length info propagates.

```python
mp[num] = mp[num-1] + mp[num+1] + 1
mp[num - mp[num-1]] = mp[num]
mp[num + mp[num+1]] = mp[num]
```

* **Time Complexity**: `O(N)` average.
* **Space Complexity**: `O(N)` for the map.

✅ More advanced, avoids redundant streak scans.
❌ Trickier to implement and understand compared to hash set.

---

## Why Hash Set (Approach 2) is Preferred

* Cleaner, easier to reason about.
* Strict `O(N)` in practice.
* Less prone to edge-case bugs than hash map method.

---

## Similar Problems (Same Pattern)

* **Longest Substring Without Repeating Characters (LeetCode 3)** → set-based uniqueness checking.
* **Longest Increasing Subsequence (LeetCode 300)** → DP version of sequence building.
* **Longest Harmonious Subsequence (LeetCode 594)** → frequency map based consecutive sequence.

---

📌 **Pattern Takeaway**:
This is the **Hashing + Sequence Detection** pattern.
Key idea: *use a hash set/map to quickly detect sequence starts and extend efficiently.*

---

# Longest Consecutive Sequence — Comparison Table

| Approach                        | Idea / Mechanism                                                                | Time Complexity     | Space Complexity | Pros ✅                                 | Cons ❌                           |
| ------------------------------- | ------------------------------------------------------------------------------- | ------------------- | ---------------- | -------------------------------------- | -------------------------------- |
| **Brute Force**                 | For each number, extend streak forward while next exists in set                 | `O(N^2)` worst case | `O(N)`           | Very easy to implement                 | Extremely slow on large inputs   |
| **Hash Set Optimized**          | Only start a streak if `num-1` not in set; extend forward to find streak length | `O(N)`              | `O(N)`           | Clean, efficient, widely used          | Still scans forward per sequence |
| **Hash Map (Union-Find style)** | Track lengths of sequences via boundaries in a hashmap; merge as needed         | `O(N)` average case | `O(N)`           | Avoids rescanning, elegant for merging | Harder to implement + debug      |

---

### ✅ Practical Takeaway

* For interviews → **Hash Set Optimized** is the safest, most understandable choice.
* For competitive programming → Hash Map method can be faster when merging multiple intervals.
* Brute Force → only for learning / warm-up, never in production.

---


