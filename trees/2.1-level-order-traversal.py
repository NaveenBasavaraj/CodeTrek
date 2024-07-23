'''
Level Order Traversal of Binary Tree

Given a binary tree root, return the level order traversal of it as a nested list, 
where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Input: root = [1]
Output: [[1]]

'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    queue = deque()
    level = 0
    result = []

    if root:
        queue.append(root)
    
    while queue:
        val = []
        for i in range(len(queue)):
            curr = queue.popleft()
            val.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        result.append(val)
        level +=1
    return result

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
    print(level_order_traversal(root))
