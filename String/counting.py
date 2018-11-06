from collections import defaultdict
M, N = map(int, input().split())
gA = [input() for _ in range(M)]
gB = [input() for _ in range(N)]
A_dict = defaultdict(list)
for i, word in enumerate(gA):
    A_dict[word].append(i + 1)
for word in gB:
    if word in A_dict:
        print (' '.join([str(s) for s in A_dict[word]]))
    else:
        print -1
