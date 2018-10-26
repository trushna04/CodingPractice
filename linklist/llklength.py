
class Node:

    def __init__(me,info):
        me.info =info
        me.next = None

class LinkedList:
    def __init__(me):
        me.head = None

    def push(me, new_info):
        new_node = Node (new_info)
        new_node.next = me.head
        me.head = new_node
    def getCount(me):
        temp = me.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
if __name__ == '__main__':
    llist = LinkedList ()
    llist.push (23)
    llist.push (12)
    llist.push (55)
    llist.push (79)
    llist.push (1)
    print ( "Count of nodes is :", llist.getCount () )