class Node:

    def __init__(me, info, nextNode=None):
        me.info = info
        me.nextNode = nextNode

    def getinfo(me):
        return me.info

    def setinfo(me, val):
        me.info = val

    def getNextNode(me):
        return me.nextNode

    def setNextNode(me, val):
        me.nextNode = val


class LinkedList:

    def __init__(me, head=None):
        me.head = head
        me.size = 0

    def getSize(me):
        return me.size

    def addNode(me, info):
        newNode = Node (info, me.head )
        me.head = newNode
        me.size += 1
        return True

    def printNode(me):
        curr = me.head
        while curr:
            print ( curr.info)
            curr = curr.getNextNode ()


myList = LinkedList ()
print ( "Inserting" )
print ( myList.addNode ( 5 ) )
print ( myList.addNode ( 10 ) )
print ( myList.addNode ( 8 ) )
print ( myList.addNode ( 9 ) )
print ( myList.addNode ( 22) )
print ( myList.addNode ( 20) )
print ( "Printing" )
myList.printNode ()
print ( "Size" )
print ( myList.getSize () )