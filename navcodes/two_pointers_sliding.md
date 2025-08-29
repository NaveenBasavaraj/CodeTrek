

---

# 📘 @notes: Two Pointers & Sliding Window

---

## 🔹 1. Two Pointers Technique

### 👉 What it means

* Use **two indices (pointers)** to traverse an array/string.
* Instead of scanning the array multiple times, we use both pointers to reduce work.
* Patterns:

  * **Opposite ends moving towards center** (palindrome, sorted 2-sum).
  * **Same direction (fast & slow pointers)** (linked list cycles, removing duplicates).

---

### ✅ Common Uses

1. **Palindrome Check** (start vs end).
2. **Two Sum in sorted array** (move left/right pointer).
3. **Remove duplicates from sorted array** (slow/fast pointer).
4. **Linked list cycle detection** (Floyd’s slow & fast pointer).

---

### 📖 Example 1: Palindrome Check

```python
def isPalindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
    return True
```

* Time: O(n)
* Space: O(1)

---

### 📖 Example 2: Two Sum (sorted array)

```python
def twoSum(nums, target):
    l, r = 0, len(nums)-1
    while l < r:
        cur = nums[l] + nums[r]
        if cur == target:
            return [l, r]
        elif cur < target:
            l += 1
        else:
            r -= 1
```

* Move pointers based on sum compared to target.

---

### 📖 Example 3: Remove Duplicates

```python
def removeDuplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

* **Slow pointer** = last unique element.
* **Fast pointer** = scanning array.

---

---

## 🔹 2. Sliding Window Technique

### 👉 What it means

* A **window (subarray or substring)** that expands/contracts over the input.
* Use two pointers (`left`, `right`) to **slide the window** across.
* Often used to find subarrays/substrings with certain properties.

---

### ✅ Common Uses

1. **Subarray with max sum** (Kadane’s, fixed-size window).
2. **Smallest subarray with condition** (min length ≥ target sum).
3. **Longest substring with unique chars** (LeetCode 3).
4. **Counting problems** (at most k distinct chars).

---

### 📖 Example 1: Fixed-size Window (max sum of k elements)

```python
def maxSum(nums, k):
    windowSum = sum(nums[:k])
    maxSum = windowSum
    for i in range(k, len(nums)):
        windowSum += nums[i] - nums[i-k]   # slide window
        maxSum = max(maxSum, windowSum)
    return maxSum
```

* Efficient because we **reuse previous sum** instead of recalculating.

---

### 📖 Example 2: Variable Window (longest substring without repeat)

```python
def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    maxLen = 0
    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1   # shrink window
        seen[ch] = r
        maxLen = max(maxLen, r-l+1)
    return maxLen
```

* Expands `r`, shrinks `l` when duplicates appear.

---

### 📖 Example 3: Smallest Subarray ≥ Target Sum

```python
def minSubArrayLen(target, nums):
    l, total = 0, 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r-l+1)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res
```

* Shrinks window when condition is satisfied.

---

---

## 🔹 Cheat Sheet Table

| Technique                          | When to Use                       | Key Pattern                                  | Example Problems                                    |
| ---------------------------------- | --------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| **Two Pointers (Opposite Ends)**   | Compare symmetric elements        | `l=0, r=n-1` move inward                     | Palindrome check, Two Sum (sorted)                  |
| **Two Pointers (Fast/Slow)**       | Detect cycles, skip duplicates    | Move `fast` quicker than `slow`              | Linked List cycle, Remove Duplicates                |
| **Sliding Window (Fixed Size)**    | Subarray of exact length k        | Expand `r`, shrink `l` after k steps         | Max sum subarray of size k                          |
| **Sliding Window (Variable Size)** | Subarray/substring with condition | Expand `r`, shrink `l` when condition breaks | Longest substring w/o repeat, Min subarray ≥ target |
| **Expand/Shrink Window**           | Optimize substring/sequence       | `while condition:` shrink left               | At most K distinct chars                            |

---

## 🔹 How to Remember

* If **comparing two sides → Two Pointers**.
* If **subarray/substring problem → Sliding Window**.
* If **window size fixed → add/remove elements while sliding**.
* If **window size variable → shrink when condition breaks**.

---

