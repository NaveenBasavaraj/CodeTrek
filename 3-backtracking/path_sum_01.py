'''
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:

'''

def hasPathSum(root_node, targetSum):
    if not root:
        return False
    
    de = [
        (root, targetSum - root_node.value)
    ]

    while de:
        node, curr_sum = de.pop()
        if not root_node.left and not root_node.right and curr_sum == 0:
            return True
        if root_node.right:
            de.append((root_node.right, curr_sum - root_node.right.value))
        if root_node.left:
            de.append((root.left, curr_sum - root_node.left.value))
    return False
    
