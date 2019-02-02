
from itertools import *
N = input()
st = input().split()
K = input()
ind = list()
com = list(combinations(range(1,(N+1),K))
for i,g in enumerate((st))
    if g == 'a'
         ind.append(i+1)
count = 0
print (float(len(set([y for x in ind for y in com if x in y ]))))/len(com)