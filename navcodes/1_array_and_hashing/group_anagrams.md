# Group Anagrams — Notes

## Problem Understanding

We are given a list of words and need to group them such that all **anagrams** fall into the same group.

* Example: `["eat", "tea", "ate"]` → same group, since all are rearrangements of each other.

This is a **string hashing / grouping** problem.

---

## Approaches

### 1. **Sorted String as Key**

* **Idea**: Anagrams, when sorted, produce the same string.
* **Algo**:

  1. For each word, sort the characters → use as key.
  2. Append word to dictionary bucket.
  3. Return grouped values.

```python
for word in words:
    key = ''.join(sorted(word))
    res[key].append(word)
```

* **Time Complexity**:

  * Sorting each word → `O(K log K)` (K = word length).
  * For N words → `O(N * K log K)`.
* **Space Complexity**:

  * Dictionary + sorted strings → `O(N*K)`.

✅ Simple, intuitive.
❌ Sorting makes it slower for long words.

---

### 2. **Character Count as Key** (Optimized, used in fix)

* **Idea**: Anagrams have identical character frequencies.
* **Algo**:

  1. Build a **26-length frequency array** per word.
  2. Convert it into a tuple (hashable).
  3. Use tuple as dict key, append word.

```python
for word in words:
    count = [0] * 26
    for ch in word:
        count[ord(ch) - ord('a')] += 1
    res[tuple(count)].append(word)
```

* **Time Complexity**:

  * Counting characters → `O(K)` (no sorting).
  * For N words → `O(N*K)`.
* **Space Complexity**:

  * Dictionary keys: tuples of size 26 → `O(26*N)` \~ `O(N)`.

✅ Faster than sorting, especially for long strings.
✅ Deterministic key, no extra sorting.
❌ Slightly more verbose.

---

## Why Method 2 is Better

* Sorting approach (`O(N*K log K)`) is **easier** to implement but slower.
* Counting approach (`O(N*K)`) is **more efficient** and scales better for larger input sizes.

---

## Similar Problems (Same Pattern)

* **Valid Anagram (LeetCode 242)** → check if two strings are anagrams using sorting or char count.
* **Find All Anagrams in a String (LeetCode 438)** → sliding window + char counts.
* **Group Shifted Strings (LeetCode 249)** → similar grouping using normalized keys.

---

📌 **Pattern Takeaway**:
This falls under the **Hashing + String Normalization** pattern.
Key idea: *map each string to a canonical representation (sorted form / frequency signature), then bucket them*.

---
