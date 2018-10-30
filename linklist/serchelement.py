class Node:
    def __init__(me,info):
        me.info = info
        me.next = None
class LinkedList:

    def __init__(me):
        me.head = None
    def push(me, new_info):
        new_node = Node(new_info)
        new_node.next = me.head
        me.head = new_node
    def search(me, li, key):
        if (not li):
            return False
        if (li.info== key):
            return True
        return me.search ( li.next, key )
if __name__ == '__main__':

    li = LinkedList ()

    li.push (23)
    li.push (99)
    li.push (56)
    li.push (47)

    key = 4

    if li.search(li.head, key):
        print ("Yes")
    else:
        print ("No")