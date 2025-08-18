class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree:
    def search(self, root, target):
        if not root:
            return False
        
        if target > root.val:
            return self.search(root.right, target)
        elif taget < root.val:
            return self.search(root.left, target):
        else:
            return True
    
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        return root
    
    def delete(self, root, val):
        
