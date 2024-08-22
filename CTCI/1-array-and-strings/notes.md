## Array and Strings

* Array questions and String questions are interchangeable.
* A question on array and be instead asked as a string

### Hash Tables

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
    
    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]
    
    def hash_function(self, key):
        # Basic hash function using modulo operation
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].insert(key, value)
    
    def get(self, key):
        index = self.hash_function(key)
        return self.table[index].find(key)

# Example usage:
hash_table = HashTable(10)

# Insert some key-value pairs
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

# Retrieve values
print(hash_table.get("apple"))  # Output: 1
print(hash_table.get("banana")) # Output: 2
print(hash_table.get("orange")) # Output: 3
print(hash_table.get("grape"))  # Output: None (not found)

```