class LinkedList ( object ):
    def __init__(me):
        me.head = None
    class Node ( object ):
        def __init__(me, d):
            me.data = d
            me.next = None
    def swapNodes(me, x, y):
        if x == y:
            return
        preX = None
        curX = me.head
        while curX != None and curX!= x:
            preX = curX
            curX = curX.next
        preY = None
        curY = me.head
        while curY != None and curY!= y:
            preY = curY
            curY = curY.next
        if curX == None or curY == None:
            return
        if preX != None:
            preX.next = curY
        else:
            me.head = curY
        if preY != None:
            preY.next = curX
        else:
            me.head = curX
        temp = curX.next
        curX.next = curY.next
        curY.next = temp
    def push(me, new_data):
        new_Node = me.Node ( new_data )
        new_Node.next = me.head
        me.head = new_Node
    def printList(me):
        tNode = me.head
        while tNode != None:
            print(tNode.data)
            tNode = tNode.next
llist = LinkedList ()
llist.push (66)
llist.push (36)
llist.push (79)
llist.push (2)
llist.push (11)
llist.push (55)
llist.push (98)
print
"Linked list before calling swapNodes() "
llist.printList ()
llist.swapNodes ( 4, 3 )
print
"\nLinked list after calling swapNodes() "
llist.printList ()
