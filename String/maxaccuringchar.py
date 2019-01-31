
ASCII_SIZE = 256


def getMaxOccuringChar(str):
    cou= [ 0 ] * ASCII_SIZE
    max = -1
    c = ''
    for i in str:
        cou[ ord ( i ) ] += 1;
    for i in str:
        if max < cou[ ord ( i ) ]:
            max = cou[ ord ( i ) ]
            c = i
    return c
str = "Apple"
print ("Max occurring character is " + getMaxOccuringChar ( str ))