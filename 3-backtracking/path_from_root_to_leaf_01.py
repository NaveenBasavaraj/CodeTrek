class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def canReachLeaf(root_node):
    '''
    Determine if a path exists from root to leaf (without containing zeroes)
    '''
    if not root_node or root_node.value == 0:
        return False # i.e  has zero hence false
    
    if not root_node.left and not root_node.right:
        return True # reached leaf
    
    if canReachLeaf(root_node.left) or canReachLeaf(root_node.right):
        # if either left or right subtree can reach leaf without zero
        return True
    return False

def canReachLeafPath(root_node,path):
    '''
    returns the path if we can reach the leaf from root
    '''
    if not root_node or root_node.value == 0:
        return False
    path.append(root.val)
    
    if not root_node.left or not root_node.right:
        return True
    
    if canReachLeafPath(root_node.left, path):
        return True
    if canReachLeafPath(root_node.right, path):
        return True
    path.pop()
    return False