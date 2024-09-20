# Problem Statement

**String Compression**

You need to compress a string using the counts of repeated characters. For example, the string "aabcccccaaa" would be compressed to "a2b1c5a3". If the compressed string is not shorter than the original string, return the original string.

### Solution

#### 1. **String Compression Algorithm**

- **Logic**:
  1. **Initialize Variables**: Use a list to build the compressed string and a counter to count consecutive characters.
  2. **Iterate Through String**: Loop through the string:
     - **Check for Change**: If the current character is different from the previous one, append the previous character and its count to the compressed list.
     - **Update Counter**: Reset the counter for the new character.
  3. **Finalize Compression**: After the loop, append the last character and its count.
  4. **Return Result**: Convert the list to a string and compare its length with the original string. Return the shorter one.
  
  **Time Complexity**: O(N), where N is the length of the string. Space complexity is O(N) for storing the compressed result.

```python
def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # Add the last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # Return the shorter of the original or compressed string
    return min(string, "".join(compressed), key=len)
```

### Summary of the Method

- **Steps**:
  1. **Initialize**: Create an empty list for the compressed string and a counter for consecutive characters.
  2. **Iterate**: Loop through the string to count characters and detect changes.
  3. **Finalize**: Append the count of the last character.
  4. **Return**: Compare lengths of the original and compressed strings and return the shorter.

- **Complexity**:
  - **Time**: O(N) — The function processes each character of the string once.
  - **Space**: O(N) — The compressed string is built as a list and converted back to a string.

This method ensures that the string is compressed efficiently, and the compressed result is only used if it is shorter than the original string.
