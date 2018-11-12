class Node:

    def __init__(me, data):
        me.data = data
        me.next = None

class LinkedList:

    def __init__(me):
        me.head = None
    def push(me, new_data):
        new_node = Node ( new_data )
        new_node.next = me.head
        me.head = new_node
    def getNth(me, index):
        current = me.head
        count = 0
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        assert (false)
        return 0;
if __name__ == '__main__':
    llist = LinkedList ()

    llist.push ( 12 );
    llist.push ( 41 );
    llist.push ( 31 );
    llist.push ( 2 );
    llist.push ( 6 );

    n = 3
    print ( "Element at index 3 is :", llist.getNth ( n ) )