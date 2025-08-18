class DFS:
    def inorder(self, root):
        '''
        left - rootval - right
        '''
        if not root:
            return
        
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)
    
    def preorder(self, root):
        '''
        rootval - left - right
        '''
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        '''
        left - right - root
        '''
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
    