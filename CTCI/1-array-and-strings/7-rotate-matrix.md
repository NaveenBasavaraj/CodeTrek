# Problem Statement

**Rotate Matrix**

Given an NxN matrix, rotate it 90 degrees clockwise. This transformation should be done in-place without using additional matrices or data structures (unless specified otherwise).

### Solutions

#### 1. **In-place Rotation (Layer by Layer)**

- **Logic**:
  1. **Identify Layers**: Treat the matrix as consisting of concentric layers. Each layer is a ring around the central part of the matrix.
  2. **Process Each Layer**: For each layer, perform the following steps:
     - **Save Top**: Store the top element temporarily.
     - **Rotate Elements**: Move elements from left to top, bottom to left, right to bottom, and top to right.
  3. **Complete Rotation**: Continue this for all layers from outermost to innermost.
  
  **Time Complexity**: O(N^2), where N is the dimension of the matrix. Each element is moved exactly once.

```python
def rotate_matrix(matrix):
    """Rotates a matrix 90 degrees clockwise."""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save top
            top = matrix[layer][i]

            # Left -> Top
            matrix[layer][i] = matrix[-i - 1][layer]

            # Bottom -> Left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # Right -> Bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # Top -> Right
            matrix[i][-layer - 1] = top
    return matrix
```

#### 2. **Double Swap Method**

- **Logic**:
  1. **Transpose Matrix**: Swap elements across the main diagonal. This converts rows into columns.
  2. **Reverse Each Row**: After transposing, reverse each row to complete the 90-degree rotation.
  
  **Time Complexity**: O(N^2). The transpose and row-reversal operations each traverse the matrix once.

```python
def rotate_matrix_double_swap(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp
    return matrix
```

#### 3. **Pythonic Approach (Using List Comprehensions)**

- **Logic**:
  1. **Transpose and Reverse**: Create a new matrix where each element is placed based on the transposed positions, then reverse the rows.
  
  **Time Complexity**: O(N^2) due to the creation of the new matrix and the nested iterations.

```python
def rotate_matrix_pythonic(matrix):
    """Rotates a matrix 90 degrees clockwise."""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # Create a new matrix
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result
```

#### 4. **Pythonic Alternate Approach (Using `zip` and `reversed`)**

- **Logic**:
  1. **Transpose and Reverse**: Transpose the matrix using `zip`, then reverse each row using `reversed`.
  
  **Time Complexity**: O(N^2). This approach also involves traversing the matrix and reversing rows.

```python
def rotate_matrix_pythonic_alternate(matrix):
    """Rotates a matrix 90 degrees clockwise."""
    return [list(reversed(row)) for row in zip(*matrix)]
```

### Summary of Each Method

1. **In-place Rotation (Layer by Layer)**:
   - **Steps**: Process matrix in layers, rotating elements within each layer.
   - **Complexity**: O(N^2) time, O(1) space (in-place).

2. **Double Swap Method**:
   - **Steps**: Transpose the matrix, then reverse each row.
   - **Complexity**: O(N^2) time, O(1) space (in-place).

3. **Pythonic Approach (Using List Comprehensions)**:
   - **Steps**: Create a new matrix by transposing and then placing elements.
   - **Complexity**: O(N^2) time, O(N^2) space (new matrix).

4. **Pythonic Alternate Approach (Using `zip` and `reversed`)**:
   - **Steps**: Transpose and reverse using built-in functions.
   - **Complexity**: O(N^2) time, O(N^2) space (new matrix).

Each approach achieves the goal of rotating the matrix 90 degrees clockwise, with differences in implementation and space usage.
