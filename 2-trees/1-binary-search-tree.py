class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = root

    def search(self, target):
        if self.root:
            return False
        if target > self.root.val:
            return self.search(self.root.right, target)
        elif target < self.root.val:
            return self.search(self.root.left, target)
        else:
            return True
    
    def insert(self, val):
        if not self.root:
            return TreeNode(val)
        
        if val > root.val:
            self.root.right = insert(self.root.right, val)
        elif val < self.root.val:
            self.root.left = insert(self.root.left, val)
        return root
    
    def minValueNode(self):
        curr = self.root
        while curr and curr.left:
            curr = curre.left
        return curr
    
    def remove(self, val):
        if not self.root:
            return None
        
        if val > self.root.val:
            self.root.right = self.remove(self.root.right, val)
        elif val < self.root.val:
            self.root.left = self.remove(self.root.left, val)
        else:
            if not self.root.left:
                return self.root.right
            elif not self.root.right:
                return self.root.left
            else:
                minNode = self.minValueNode(self.root.right)
                self.root.val = minNode.val
                self.root.right = remove(self.root.right, minNode.val)
        return self.root