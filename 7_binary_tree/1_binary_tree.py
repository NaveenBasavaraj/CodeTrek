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
    
    def search(self, node, target):
        if not node:
            return False
    
        if target > node.val:
            return search(node.right, target)
        elif target < node.val:
            return search(node.left, target)
        else:
            return True
    
    def remove(node, val):
        if not node:
            return None

        if val > node.val:
            node.right = remove(node.right, val)
        elif val < node.val:
            node.left = remove(node.left, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                minNode = minValueNode(node.right)
                node.val = minNode.val
                node.right = remove(node.right, minNode.val)
        return node
