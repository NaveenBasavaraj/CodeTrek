### /codemd

# Valid Sudoku — Notes

## Problem Understanding

We need to validate a **9×9 Sudoku board**.
Rules of Sudoku:

1. Each row must contain digits `1–9` without repetition.
2. Each column must contain digits `1–9` without repetition.
3. Each 3×3 sub-grid (square) must contain digits `1–9` without repetition.
4. Empty cells are represented by `"."` and can be ignored.

This is a **constraint checking problem**.

---

## Approaches

### 1. **Using HashSets (Optimal Approach)**

* **Idea**: Track seen digits for rows, cols, and squares using hash sets.
* **Algorithm**:

  1. Create `rows`, `cols`, `squares` as dictionaries of sets.
  2. For each cell `(r, c)`:

     * Skip if `"."`.
     * Check if digit exists in `rows[r]`, `cols[c]`, or `squares[(r//3, c//3)]`.

       * If yes → invalid.
     * Else add digit to all three.
  3. If no conflicts → board is valid.

```python
for r in range(9):
    for c in range(9):
        if board[r][c] == ".": continue
        if (board[r][c] in rows[r] or 
            board[r][c] in cols[c] or 
            board[r][c] in squares[(r//3, c//3)]):
            return False
        rows[r].add(board[r][c])
        cols[c].add(board[r][c])
        squares[(r//3, c//3)].add(board[r][c])
```

* **Time Complexity**: `O(1)` per cell → `O(9×9) = O(81)` → constant time.
* **Space Complexity**: `O(81)` for sets.

✅ Efficient, clean.
✅ Runs in constant time since board size is fixed.

---

### 2. **Brute Force Check** (Not efficient but intuitive)

* For each row, check if digits repeat.
* For each column, check if digits repeat.
* For each 3×3 block, check if digits repeat.
* **Time Complexity**: still `O(81)` but requires multiple passes.
* **Space Complexity**: `O(1)` if using arrays.

❌ Multiple redundant scans.
✅ Simple to reason about.

---

## Why Method 1 is Better

* **Single pass** → checks all constraints while scanning once.
* Cleaner and more extensible.
* Brute force feels simpler, but less elegant and involves more bookkeeping.

---

## Similar Problems (Same Pattern)

* **Sudoku Solver (LeetCode 37)** → backtracking extension of this problem.
* **N-Queens** → place queens on a board with row/col/diagonal constraints.
* **Latin Square Validation** → similar row/col uniqueness checks.

---

📌 **Pattern Takeaway**:
This is a **constraint satisfaction + hash set lookup** pattern.
Key idea: *track seen values in constant-time structures while scanning once*.

---

Do you want me to also create a **step-by-step dry run** of the hash set method with a small board so you can see how rows, cols, and squares evolve?
