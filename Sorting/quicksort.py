

def quicksort(listToSort,low,high):
    if((high-low)>0):
        p = partition(listToSort,low,high)
        quicksort(listToSort,low,p-1)
        quicksort(listToSort,p+1,high)

def partition(listToSort,lowIndex,highIndex):
    divider = lowIndex
    pivot= highIndex

    for i in range(lowIndex,highIndex):
        if(listToSort[i]<listToSort[pivot]):
            listToSort[i],listToSort[divider]= listTosort[divider],listToSort[i]
            divider +=1

    listTosort[pivot],listToSort[divider]= listToSort[divider],ListToSort[pivot]

    return divider
A=[1,0,7,9,8,4,6,0]
quicksort(A,0,9)
print(A)
