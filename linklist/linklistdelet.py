class Node:

    def __init__(me,info):
        me.info = info
        me.next = None

class LinkedList:

    def __init__(me):
        me.head = None

    def deleteList(me):
        curr = me.head
        while curr:
            pre= curr.next
            del curr.info
            curr= pre
    def push(me, new_info):
        new_node = Node ( new_info )
        new_node.next = me.head
        me.head = new_node

    if __name__ == '__main__':

        llist = LinkedList()
        llist.push (11)
        llist.push (14)
        llist.push (21)
        llist.push (12)
        llist.push (71)

    print("Deleting")
    llist.deleteList()

    print ( "Linked list deleted" )

