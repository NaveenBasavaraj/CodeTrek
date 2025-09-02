### /codemd

# Product of Array Except Self — Notes

## Problem Understanding

We are asked to return an array where each element at index `i` is the **product of all elements in the array except `nums[i]`**, without using division.

Example:

* Input: `[1,2,3,4]`
* Output: `[24,12,8,6]`

---

## Approaches

### 1. **Naive Approach (Brute Force)**

* For each index `i`, multiply all numbers except `nums[i]`.
* **Time Complexity**: `O(N^2)`
* **Space Complexity**: `O(1)`
  ❌ Too slow for large arrays.

---

### 2. **Using Division (Not Allowed in LeetCode)**

* Compute `total_product = product(nums)`.
* Each result = `total_product / nums[i]`.
* **Problem**: Division not allowed + fails with zeros.

---

### 3. **Prefix and Postfix Products (Optimal)** ✅

* **Idea**: Each element’s result = product of all numbers before it (prefix) × product of all numbers after it (postfix).
* **Steps**:

  1. Create result array initialized to `1`.
  2. Forward pass → store prefix product at each index.
  3. Backward pass → multiply by postfix product.

```python
# Prefix pass
prefix = 1
for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

# Postfix pass
postfix = 1
for i in range(len(nums)-1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
```

* **Time Complexity**: `O(N)`
* **Space Complexity**: `O(1)` (excluding output).

---

## Why Prefix–Postfix Method is Better

* Handles zeros correctly.
* Avoids division entirely.
* Single scan forward + backward → efficient.

---

## Similar Problems (Same Pattern)

* **Trapping Rain Water (LeetCode 42)** → left and right prefix maxima.
* **Minimum Product Subarray** → prefix/postfix ideas applied to products.
* **Running Sum of Array (LeetCode 1480)** → prefix sums instead of products.

---

📌 **Pattern Takeaway**:
This is the **Prefix–Suffix Product pattern**.
Key idea: *compute cumulative results from left and right, then combine*.

---

