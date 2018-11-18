def sibling(s, p):

parent = s.parent(p)
if parent is None:
    print(None)
else:
    if p == s.left(parent):
        print (s.right(parent))
    else:
        print(s.left(parent))

def children(s, p):
    if s.left(p) is not None:
        yield s.left(p)
    if s.right(p) is not None:
        yield s.right(p)
