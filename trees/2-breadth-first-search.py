
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def breadth_first_search(root):
    '''
    breadth first traversal and print the values
    '''
    queue = deque()
    level = 0
    if root:
        # basically a deque, append on the right and pop from left
        queue.append(root)
    
    
    while queue:
        print("level: ", level)
        for i in range(len(queue)):
            # pop the root and print
            # take the children in the deque
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

    
if __name__ == "__main__":
    # Example usage
    # Create a binary tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Perform BFS traversal and print the levels
    breadth_first_search(root)