def merge(lef,righ):
	result = []
	i,j = 0, 0
	while i<len(lef) and j< len(righ):
		if lef[i] <= righ[j]:
			result.append(lef[i])
			i+=1
		else:
			result.append(righ[j])
			j+=1

	result += lef[i:]
	result += righ[j:]
	return result


def mergesort(lst):
	if(len(lst) <= 1):
		return lst
	mid = int(len(lst)/2)
	left = mergesort(lst[:mid])
	right = mergesort(lst[mid:])
	return merge(left,right)


arr = [1,2,-1,0,9,65,7,3,4,1,2]
print(mergesort(arr))
