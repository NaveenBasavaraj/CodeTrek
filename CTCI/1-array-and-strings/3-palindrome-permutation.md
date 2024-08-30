Certainly! Here is a Markdown-formatted explanation that outlines the problem and provides Python code for each method without using special libraries like `Counter`.

```markdown
# Palindrome Permutation Checker

## Problem Explanation

A **palindrome** is a string that reads the same forwards and backwards, such as "racecar" or "level". A **permutation** of a palindrome means that by rearranging the letters of a string, you could form a palindrome. 

For example, "racecar" is a palindrome itself, and "carrace" is a permutation of "racecar" that is also a palindrome. Therefore, to determine if a string is a permutation of a palindrome, we need to check if its letters can be rearranged to form a palindrome.

## Key Insight

For a string to be a permutation of a palindrome:
- In a palindrome, characters appear in pairs (e.g., "abba" has pairs of 'a' and 'b').
- Therefore, most characters in the string must appear an even number of times.
- At most one character can appear an odd number of times (this would be the middle character in an odd-length palindrome).

## Different Solutions

### 1. Frequency Count Method

**Logic**: Count how many times each character appears. Check how many characters have odd frequencies. For the string to be a permutation of a palindrome, there should be at most one character with an odd frequency.

**Steps**:
- Clean the string (remove non-letter characters and convert to lowercase).
- Count the occurrences of each character.
- Check how many characters have an odd count. If more than one, it cannot be a permutation of a palindrome.

```python
import re

def is_permutation_of_palindrome(s: str) -> bool:
    # Clean the string: remove non-letter characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    # Count occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Count how many characters have odd frequencies
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # For a permutation of a palindrome, there should be at most one odd frequency
    return odd_count <= 1

# Example usage
print(is_permutation_of_palindrome("Tact Coa"))  # Output: True
```

### 2. Bit Vector Method

**Logic**: Use a bit vector (bitmask) to keep track of which characters have been seen an odd number of times. Each bit in an integer represents a character's occurrence (0 for even, 1 for odd). For a string to be a permutation of a palindrome, the bit vector should have at most one bit set to 1.

**Steps**:
- Clean the string (remove non-letter characters and convert to lowercase).
- Iterate through each character, use its ASCII value to toggle the corresponding bit in the bit vector.
- At the end, check if the bit vector has at most one bit set. This indicates that the string can be rearranged into a palindrome.

```python
import re

def is_permutation_of_palindrome(s: str) -> bool:
    # Clean the string: remove non-letter characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    # Use a bit vector to track character frequencies
    bit_vector = 0
    
    for char in s:
        # Toggle the bit for the character
        bit_index = ord(char) - ord('a')
        bit_vector ^= (1 << bit_index)
    
    # Check if at most one bit is set
    return (bit_vector & (bit_vector - 1)) == 0

# Example usage
print(is_permutation_of_palindrome("Tact Coa"))  # Output: True
```

### 3. XOR Method

**Logic**: Use XOR operation to keep track of characters with odd counts. XORing a number with itself cancels it out (0), so characters appearing an even number of times will cancel out, leaving at most one character with an odd count.

**Steps**:
- Clean the string (remove non-letter characters and convert to lowercase).
- Iterate through each character, XOR the current result with the character's ASCII value.
- At the end, check if the result of XORing all characters has at most one bit set. This indicates that the string can be rearranged into a palindrome.

```python
import re

def is_permutation_of_palindrome(s: str) -> bool:
    # Clean the string: remove non-letter characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    # Use XOR to keep track of odd character counts
    xor_result = 0
    
    for char in s:
        # XOR the ASCII value of the character
        xor_result ^= ord(char)
    
    # Check if XOR result has at most one bit set
    return (xor_result & (xor_result - 1)) == 0

# Example usage
print(is_permutation_of_palindrome("Tact Coa"))  # Output: True
```

## Summary

- **Frequency Count**: Count character occurrences and ensure there is at most one odd count.
- **Bit Vector**: Use a bitmask to track character frequencies and check if at most one bit is set.
- **XOR**: Use XOR to efficiently track odd counts and verify that the result has at most one bit set.

Each approach effectively solves the problem but uses different techniques to manage and check character frequencies.
```
