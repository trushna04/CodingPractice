class Node:
    def init(d, key):
        d.left = None
        d.right = None
        d.val = key
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
