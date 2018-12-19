class Tushi:

    def __init__(me, limit):
        me.limit = limit
    def __iter__(me):
        me.x = 5
        return me
    def next(me):

        x = me.x
        if x > me.limit:
            raise StopIteration
            me.x = x + 1;
        return x
for i in ( 15 ):
    print (i)