class Node:
    def __init__(da, key):
        da.left = None
        da.right = None
        da.val = key
def printPost(root):
    if root:
        printPost(root.left)
        printPost(root.right)
        print(root.val)
def printPre(root):
    if root:
        print(root.val)
        printPre(root.left)
        printPre(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPre(root)
print("\nPostorder traversal of binary tree is")
printPost(root)