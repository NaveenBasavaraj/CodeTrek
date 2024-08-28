### Problem Statement

**String Rotation**

Given two strings, `s1` and `s2`, determine if `s2` is a rotation of `s1`. For example, if `s1` is "waterbottle", then `s2` could be "erbottlewat" because it is a rotation of `s1`.

### Solution

#### **Using String Concatenation**

- **Logic**:
  1. **Length Check**: First, check if both strings are of the same length. If not, `s2` cannot be a rotation of `s1`.
  2. **Rotation Check**: Concatenate `s1` with itself to form a new string. This concatenated string will contain all possible rotations of `s1`. Check if `s2` is a substring of this concatenated string.
  
  **Time Complexity**: O(N), where N is the length of the strings. Concatenating `s1` with itself takes O(N) time, and checking if `s2` is a substring of this concatenated string also takes O(N) time.

```python
def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False
```

### Summary of Each Method

1. **Using String Concatenation**:
   - **Steps**:
     1. Check if the lengths of `s1` and `s2` are equal.
     2. Concatenate `s1` with itself to create a new string.
     3. Check if `s2` is a substring of the concatenated string.
   - **Complexity**:
     - **Time**: O(N) for concatenation and substring check.
     - **Space**: O(N) for storing the concatenated string.

### Example Test Cases

1. **Test Case 1**: 
   - **Input**: `s1 = "waterbottle"`, `s2 = "erbottlewat"`
   - **Output**: `True` (because "erbottlewat" is a rotation of "waterbottle")

2. **Test Case 2**:
   - **Input**: `s1 = "foo"`, `s2 = "bar"`
   - **Output**: `False` (because "bar" is not a rotation of "foo")

3. **Test Case 3**:
   - **Input**: `s1 = "foo"`, `s2 = "foofoo"`
   - **Output**: `False` (because "foofoo" is not a rotation of "foo")

This method is straightforward and leverages the properties of string rotations efficiently with minimal complexity.