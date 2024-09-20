# Problem Statement

**Determine if a String Has All Unique Characters**

You need to check if every character in a given string appears only once.

### Solutions

#### 1. **Algorithmic Approach with Array**

- **Logic**:
  1. **Check Length**: If the string length exceeds 128, return `False` (because there are only 128 unique ASCII characters).
  2. **Initialize Array**: Create a boolean array of size 128 to keep track of character occurrences.
  3. **Iterate Characters**: For each character in the string:
     - Convert the character to its ASCII value.
     - Use the ASCII value to index into the array and check if the character has been seen before.
     - If it has, return `False`.
     - Otherwise, mark the character as seen by updating the array.
  4. **Return True**: If all characters are unique, return `True`.

```python
def is_unique_chars_array(string):
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True
```

#### 2. **Pythonic Approach Using Set**

- **Logic**:
  1. **Convert to Set**: Convert the string to a set, which inherently removes duplicates.
  2. **Compare Lengths**: Compare the length of the set with the length of the original string.
  3. **Return Result**: If the lengths match, the string has all unique characters; otherwise, it does not.

```python
def is_unique_chars_set(string):
    return len(set(string)) == len(string)
```

#### 3. **Bit Vector Approach**

- **Logic**:
  1. **Check Length**: If the string length exceeds 128, return `False`.
  2. **Initialize Bit Vector**: Use an integer where each bit represents a character.
  3. **Iterate Characters**: For each character:
     - Calculate the bit position using its ASCII value.
     - Check if the bit is already set.
     - If the bit is set, return `False`.
     - Otherwise, set the bit using bitwise operations.
  4. **Return Result**: If no duplicate bits are set, return `True`.

```python
def is_unique_chars_bit_vector(string):
    if len(string) > 128:
        return False

    checker = 0
    for char in string:
        val = ord(char)
        bit = 1 << val
        if checker & bit:
            return False
        checker |= bit
    return True
```

#### 4. **Dictionary Approach**

- **Logic**:
  1. **Initialize Dictionary**: Use a dictionary to track occurrences of characters.
  2. **Iterate Characters**: For each character:
     - Check if the character is already in the dictionary.
     - If it is, return `False`.
     - Otherwise, add the character to the dictionary.
  3. **Return True**: If no duplicates are found, return `True`.

```python
def is_unique_chars_dictionary(string):
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True
```

#### 5. **Alternative Set Approach**

- **Logic**:
  1. **Initialize Set**: Use a set to keep track of seen characters.
  2. **Iterate Characters**: For each character:
     - Check if it is already in the set.
     - If it is, return `False`.
     - Otherwise, add the character to the set.
  3. **Return True**: If no duplicates are found, return `True`.

```python
def is_unique_chars_set_alternative(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True
```

#### 6. **Sorting Approach (With Extra Variable)**

- **Logic**:
  1. **Sort String**: Sort the string.
  2. **Check Adjacent Characters**: Iterate through the sorted string and check if any adjacent characters are the same.
  3. **Return Result**: If duplicates are found, return `False`. Otherwise, return `True`.

```python
def is_unique_chars_sorting(string):
    sorted_string = sorted(string)
    for i in range(1, len(sorted_string)):
        if sorted_string[i] == sorted_string[i - 1]:
            return False
    return True
```

#### 7. **In-place Sorting Approach**

- **Logic**:
  1. **Sort String**: Sort the string in-place.
  2. **Check Adjacent Characters**: Iterate through the sorted string to check for adjacent duplicates.
  3. **Return Result**: Return `False` if duplicates are found; otherwise, return `True`.

```python
def is_unique_chars_inplace_sort(string):
    sorted_string = sorted(string)
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    return True
```

### Summary of Each Method

- **Array Approach**: Uses a fixed-size boolean array to track character presence.
- **Set Approach**: Utilizes Python’s set to efficiently manage and check for uniqueness.
- **Bit Vector Approach**: Employs bitwise operations for space-efficient uniqueness checking.
- **Dictionary Approach**: Uses a dictionary to track occurrences, simple but space-consuming.
- **Alternative Set Approach**: Another straightforward implementation using sets.
- **Sorting Approach (Extra Variable)**: Sorts the string and checks adjacent characters for duplicates.
- **In-place Sorting Approach**: Similar to the sorting approach but modifies the original string.

Each method provides a different trade-off between space efficiency and implementation complexity.
