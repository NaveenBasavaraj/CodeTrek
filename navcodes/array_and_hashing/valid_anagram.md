# 🧩 Valid Anagram Problem

## Problem Statement
Given two strings `s1` and `s2`, return `True` if `s2` is an anagram of `s1`, otherwise `False`.

An **anagram** means:
- Both strings contain the **same characters**
- Characters must appear the **same number of times**
- Order **does not** matter

---

## Solutions Implemented

### 1. **Using Hashmaps (Dictionaries)**

```python
def is_valid_anagram(self, s1, s2):
    if len(s1) != len(s2):
        return False
    counts1, counts2 = {}, {}
    for i in range(len(s1)):
        counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
        counts2[s2[i]] = 1 + counts2.get(s2[i], 0)
    return counts1 == counts2
```

✔️ **How it works**
- We maintain two dictionaries that **count the frequency of each character** in both strings.  
- Finally, compare the dictionaries. If equal → strings are anagrams.

📊 **Complexity**
- Time: `O(n)` (iterating both strings once)  
- Space: `O(k)` where `k` is number of unique characters  

---

### 2. **Using Array Hashing**

```python
def is_valid_anagram_array(self, s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = [0] * 26
    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1
        count[ord(s2[i]) - ord('a')] -= 1
    for val in count:
        if val != 0:
            return False
    return True
```

✔️ **Key Idea**
- Instead of using a dictionary, use a **fixed-size array** of 26 integers (for lowercase English letters).  
- Each index represents a letter:
  - Index `0` → `'a'`
  - Index `1` → `'b'`
  - …  
  - Index `25` → `'z'`

✔️ **How `ord(char) - ord('a')` works**
- `ord('a')` = 97, `ord('b')` = 98, etc.  
- Subtracting `ord('a')` makes `'a' → 0`, `'b' → 1`, … `'z' → 25`.  
- Example: `ord('c') - ord('a') = 99 - 97 = 2`.

✔️ **Process**
- For every char in `s1` → increment its slot in `count`.  
- For every char in `s2` → decrement its slot.  
- If all slots = 0 at the end → perfect match (anagram).  

📊 **Complexity**
- Time: `O(n)`  
- Space: `O(1)` (always 26, independent of input size)

---

### 3. **Using Sorting**

```python
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

✔️ **How it works**
- Sort both strings.  
- If they are equal after sorting → they are anagrams.  

📊 **Complexity**
- Time: `O(n log n)` (due to sorting)  
- Space: `O(1)` or `O(n)` depending on sort implementation  

---

## 🔍 Method Comparison

| Method                 | Time      | Space      | Notes |
|------------------------|-----------|------------|-------|
| **Hashmap (dict)**     | `O(n)`    | `O(k)`     | Works for all Unicode chars, flexible |
| **Array Hashing (26)** | `O(n)`    | `O(1)`     | Best for lowercase English letters only |
| **Sorting**            | `O(n log n)` | `O(1)`/`O(n)` | Easiest to implement, but slower |

---

## ✅ Best Practice

- **If strings contain only lowercase English letters** → Use **array hashing** (fastest, constant space).  
- **If strings contain any characters (Unicode, symbols, etc.)** → Use **hashmap (dict)**.  
- **If you want quick and simple code** (but less efficient) → Use **sorting**.

---

## Example Walkthrough

Input: `s1 = "listen", s2 = "silent"`

1. **Hashmap Method**  
   - counts1 = `{l:1, i:1, s:1, t:1, e:1, n:1}`  
   - counts2 = `{s:1, i:1, l:1, e:1, n:1, t:1}`  
   - Equal → return `True`

2. **Array Method**  
   - For `"listen"` → increments positions for `l,i,s,t,e,n`  
   - For `"silent"` → decrements same positions  
   - All slots back to `0` → return `True`

3. **Sorting Method**  
   - sorted("listen") = `['e','i','l','n','s','t']`  
   - sorted("silent") = `['e','i','l','n','s','t']`  
   - Equal → return `True`
