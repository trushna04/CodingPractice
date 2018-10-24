class Node:

    def __init__(self,info, nextNode=None):
        self.info = info
        self.nextNode = nextNode

    def getinfo(self):
        return self.info

    def setinfo(self, val):
        self.info = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(me, head=None):
        me.head = head
        me.size = 0

    def getSize(me):
        return me.size

    def addNode(me,info):
        newNode = Node (info, me.head )
        me.head = newNode
        me.size += 1
        return True

    def printNode(me):
        curr = me.head
        while curr:
            print ( curr.info )
            curr = curr.getNextNode ()


myList = LinkedList ()
print ( "Inserting" )
print ( myList.addNode (8) )
print ( myList.addNode (2) )
print ( myList.addNode (1) )
print ( myList.addNode (5) )
print ( myList.addNode (3) )
print ( myList.addNode (7) )
print ( "Printing" )
myList.printNode ()
print ( "size" )
print ( myList.getSize () )