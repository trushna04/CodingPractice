n= int(input())
for i in range(1,n+1):
    print("The decimal value of",i,"is:")
    print(bin(i),"in binary.")
    print(oct(i),"in octal.")
    print(hex(i),"in hexadecimal.")
    i+=i
