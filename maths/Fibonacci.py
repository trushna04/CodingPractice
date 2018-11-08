n = int(input())
A= int(input())
B= int(input())
print (A,B)
x=0
while(n>2):
    x= A+B;
    A=B
    B=x
    print(x)
    n=n-1