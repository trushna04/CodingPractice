from pip._vendor.distlib.compat import raw_input

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(''.join(['.|.'] * i).center(M, '-'))
print("WELCOME".center(M, '-'))
for i in range(N-2, -1, -2):
    print(''.join(['.|.'] * i).center(M, '-'))