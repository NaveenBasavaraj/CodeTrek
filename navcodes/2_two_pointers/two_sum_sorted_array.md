### /codemd

# Two Sum (Two-Pointer Approach)

---

## 🔑 Problem Pattern

* Category: **Array + Two Pointers**
* Classic variation: *LeetCode 167. Two Sum II – Input array is sorted*
* Core idea: Use **two pointers** moving inward to find the pair.

---

## 🧩 Algorithm (Two Pointers)

1. Initialize two pointers:

   * `l = 0` (start of array)
   * `r = len(nums) - 1` (end of array).
2. Compute `curr_sum = nums[l] + nums[r]`.
3. If `curr_sum == target` → return `[l+1, r+1]` (problem requires 1-based indices).
4. If `curr_sum > target` → move right pointer left (`r -= 1`).
5. If `curr_sum < target` → move left pointer right (`l += 1`).
6. Continue until `l >= r`.

---

## ⏱️ Complexity

* **Time:** `O(N)` (single pass with two pointers).
* **Space:** `O(1)` (no extra data structures).

---

## ✅ Why This Works

* Since array is sorted, decreasing or increasing the sum can be achieved deterministically by moving pointers.
* This avoids `O(N^2)` brute force.

---

## 📌 Alternative Approaches

1. **Brute Force:**

   * Check all pairs.
   * Time: `O(N^2)` → too slow for large inputs.
2. **Hashmap (works for unsorted arrays):**

   * Use dictionary to check if `target - num` exists.
   * Time: `O(N)`, Space: `O(N)`.
   * More general, works on unsorted arrays.

---

## 🎯 Similar Problems (Same Pattern)

* **3Sum** → Extend to 3 numbers using two pointers inside a loop.
* **4Sum** → Extend further (nested loops + two pointers).
* **Container With Most Water** → Two pointers with max area optimization.
* **Valid Palindrome** → Two-pointer scan inward ignoring non-alphanumeric chars.

---

⚖️ **Tradeoff:**

* If array is sorted → Two-pointer is best (`O(N), O(1)`).
* If array is unsorted → Use Hashmap.

---
