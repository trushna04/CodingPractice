class Node:
    def __init__(me, data):
        me.data = data
        me.left = None
        me.right = None

def rLOrder(root):
    h = height(root)
    for i in reversed (range(1, h + 1)):
        printGivenLevel(root,i)
def printGivenLevel(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data)

    elif level > 1:
        printGivenLevel ( root.left, level - 1 )
        printGivenLevel ( root.right, level - 1 )

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
root = Node(1)
root.left = Node(22)
root.right = Node(33)
root.left.left = Node(45)
root.left.right = Node(56)

print ("Level Order traversal of binary tree is")
rLOrder(root)