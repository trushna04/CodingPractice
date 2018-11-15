def bsearch(list, val):

    list_size = len(list) - 1

    id0 = 0
    idn = list_size

    while id0 <= idn:
        midval = (id0 + idn)// 2

        if list[midval] == val:
            return midval
        if val > list[midval]:
            id0 = midval + 1
        else:
            idn = midval - 1

    if id0 > idn:
        return None

list = [2,1,9,3,5,7]


print(bsearch(list,2))
print(bsearch(list,7))