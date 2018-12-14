class Node:


    def __init__(me, item):
        me.key = item
        me.left = None
        me.right = None

def preorder(root):
    if root is not None:
        print (root.key,)
        preorder(root.left)
        preorder(root.right)

def posTrees(arr, start, end):
    trees = [ ]

    if start > end:
        trees.append ( None )
        return trees

    for i in range ( start, end + 1 ):

        ltrees = posTrees( arr, start, i - 1 )

        rtrees = posTrees( arr, i + 1, end )

        for j in ltrees:
            for k in rtrees:

                node = Node ( arr[ i ] )


                node.left = j


                node.right = k


                trees.append ( node )
    return trees



inp = [ 1,2,3,4,5,6 ]
n = len ( inp )

trees = posTrees ( inp, 0, n - 1 )

print(" possible Binary Trees are ")
for i in trees:
    preorder ( i );
    print(" ")