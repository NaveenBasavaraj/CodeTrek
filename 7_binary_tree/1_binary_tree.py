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
            node.left = _insert(node.left, value)
        elif value > node.value:
            node.right = _insert(node.right, value)
        return node