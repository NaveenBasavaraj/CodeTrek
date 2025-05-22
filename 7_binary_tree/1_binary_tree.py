class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        return node

    def search(self, node, target):
        if node is None:
            return False
        if target > node.value:
            return self.search(node.right, target)
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return True

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.remove(node.left, value)
        elif value > node.value:
            node.right = self.remove(node.right, value)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            min_node = self.min_value_node(node.right)
            node.value = min_node.value
            node.right = self.remove(node.right, min_node.value)

        return node

    def find_depth(self, node, value, depth=0):
        if node is None:
            return -1  # Value not found
        if node.value == value:
            return depth
        elif value < node.value:
            return self.find_depth(node.left, value, depth + 1)
        else:
            return self.find_depth(node.right, value, depth + 1)

    def find_height(self, node):
        if node is None:
            return -1  # Convention: height of empty node is -1
        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)
        return 1 + max(left_height, right_height)


if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert values into the tree
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.root = bst.insert(bst.root, val)

    # Search tests
    assert bst.search(bst.root, 40) == True
    assert bst.search(bst.root, 90) == False

    # Depth tests
    print("Depth of 20:", bst.find_depth(bst.root, 20))  # Expected: 2
    print("Depth of 70:", bst.find_depth(bst.root, 70))  # Expected: 1

    # Height test
    print("Height of tree:", bst.find_height(bst.root))  # Expected: 2

    # Remove node and re-check
    bst.root = bst.remove(bst.root, 70)  # Remove node with one child
    assert bst.search(bst.root, 70) == False
    print("Removed 70, new height:", bst.find_height(bst.root))

    print("All tests passed.")
