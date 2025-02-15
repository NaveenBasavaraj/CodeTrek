class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeBuilder:
    def __init__(self):
        self.root = None 
    
    def insert(self, root,  val):
        if root is None:
            return TreeNode(val)
        if val < root.value:
            root.left = self.insert(root.left, val)
        elif val > root.value:
            root.right = self.insert(root.right, val)
        return root
    
    def add(self, val):
        self.root = self.insert(self.root, val)
    
    def add_using_list(self, values):
        if not values:
            return self.root
        for val in values:
            self.add(val)
    
    def inorder_traversal(self, root):
        # to print tree
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)
    
    def min_value_node(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def remove(self, root, val):
        if not root:
            return None
        if val > root.value:
            root.right = self.remove(root.right, val)
        elif val < root.value:
            root.left = self.remove(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.min_value_node(root.right)
                root.value = minNode.value
                root.right = self.remove(root.right, minNode.value)
        return root



if __name__ == "__main__":
    tree = BinaryTreeBuilder()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)  # Expected Output: 3 5 7 10 15

    tree_list = BinaryTreeBuilder()
    tree_list.add(10)
    tree_list.add_using_list([5,15,3,7])
    print("Inorder Traversal:")
    tree_list.inorder_traversal(tree.root)

