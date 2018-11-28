class Node:
    def __init__(me, value, next=None):
        me.value = value
        me.next = next


def buildList():
    lValues = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    linkedList = None
    next = None
    lValues.reverse ()
    for x in lValues:
        linkedList = Node ( x, next )
        next = linkedList
    return linkedList


def findMiddle(linkedList):
    middle = linkedList
    current = linkedList
    odd = True
    while (current.next is not None):
        print ( "Current: " + current.value)
        if (not odd):
            middle = middle.next
        current = current.next
        odd = not odd
    print ( "Current: " + current.value, " Middle: " + middle.value)


linkedList = buildList ()
findMiddle ( linkedList )
