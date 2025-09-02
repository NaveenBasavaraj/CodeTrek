### /codemd

# Encode and Decode Strings — Notes

## Problem Understanding

We want to implement a **string encoding/decoding scheme** that can:

* Convert a list of strings → single encoded string.
* Decode back to the original list.

The tricky part:

* Strings may contain special characters (`#`, digits, spaces).
* We must avoid ambiguity during decoding.

---

## Approach

### Encoding

* For each word: prepend its **length** followed by a delimiter (here, `#`).
* Append word itself.
* Example:

  * `["lint", "code"]` → `"4#lint4#code"`.

```python
for word in words:
    encoded_str += str(len(word)) + "#" + word
```

### Decoding

* Parse string sequentially:

  1. Start at index `i`.
  2. Move `j` forward until encountering `"#"`.
  3. Convert substring `encoded_str[i:j]` → length.
  4. Extract word of given length starting from `j+1`.
  5. Append to result list.
  6. Move pointer ahead by length and repeat.

```python
while i < len(encoded_str):
    j = i
    while encoded_str[j] != "#":
        j += 1
    length = int(encoded_str[i:j])
    i = j + 1
    word = encoded_str[i:i+length]
    decoded_words.append(word)
    i += length
```

---

## Complexity Analysis

* **Encoding**:

  * Each word processed once → `O(N * K)` (N = number of words, K = avg length).
* **Decoding**:

  * Each char scanned once → `O(L)` (L = length of encoded string).
* **Space Complexity**:

  * Both encoding & decoding → `O(N*K)` (storing all words).

✅ Efficient: linear time and space.

---

## Why This Works Well

* By storing **word length before content**, we avoid ambiguity:

  * Example: `["12", "3"]` → `"2#123#3"`.
  * Decoder knows first word is length `2` → `"12"`, then second word is `"3"`.
* Works even if words contain `#` or digits.

---

## Similar Problems (Same Pattern)

* **LeetCode 271: Encode and Decode Strings** (classic problem).
* **Serialization/Deserialization of Trees (LeetCode 297)** → similar concept, encode structured data into strings.
* **Custom Compression Schemes** → prefix lengths or delimiters used to split tokens safely.

---

📌 **Pattern Takeaway**:
This is a **Serialization + Parsing** pattern.
Key idea: *prefix each piece of data with metadata (like length) so parsing is deterministic*.

---
