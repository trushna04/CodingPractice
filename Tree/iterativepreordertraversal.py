class Node:
    def __init__(me, data):
        me.data = data
        me.left = None
        me.right = None
def itvPreorder(root):

    if root is None:
        return
    nodeStack = [ ]
    nodeStack.append ( root )
    while (len ( nodeStack ) > 0):
        node = nodeStack.pop ()
        print(node.data)
        if node.right is not None:
            nodeStack.append ( node.right )
        if node.left is not None:
            nodeStack.append ( node.left )
root = Node ( 1 )
root.left = Node ( 8 )
root.right = Node ( 2 )
root.left.left = Node ( 3 )
root.left.right = Node ( 5 )
root.right.left = Node ( 2 )
itvPreorder ( root )
