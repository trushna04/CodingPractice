/* sum of two int of array and if sum ==target then print that numbers
https://leetcode.com/problems/two-sum/*/


n= [2, 7, 11, 15]
target = 9
for i in range (len(n)-1):
    for j in range (i+1,len(n)):
        if (n[i]+n[j]==target):
            print(n[i],n[j])
