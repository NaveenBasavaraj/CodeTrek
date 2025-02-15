from binary_tree import TreeNode, BinaryTreeBuilder


def search(root, target):
    if not root:
        return False
    
    if target > root.value:
        return search(root.right, target)
    elif target < root.value:
        return search(root.left, target)
    else:
        return True


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
    print(f"search values")
    print(search(tree.root, 3))
    print(search(tree.root, 13))