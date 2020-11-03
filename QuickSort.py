#퀵소트, p는 왼쪽, r은 오른쪽

def QuickSort(A,p,r):
	if p < r :
		q = partition(A,p,r,r)
		print("q: ",q)
		QuickSort(A,p,q-1)
		QuickSort(A,q+1,r)
		return A
		
def partition(A,p,r,pivot_pos):
	x = A[pivot_pos]
	i = p-1
	for k in range(p,r+1): 
		# p to r
		if (A[k] < x and k != pivot_pos) :
			if (i+1 == pivot_pos) : 
				i+=1
			i+=1
			A[i],A[k] = A[k],A[i]
	A[i+1],A[pivot_pos] = A[pivot_pos],A[i+1]
	return i+1
	
a = [3,1,8,6,10,2,4,9,7,5]
b= [3,6,2,4,1,8,7,5]
sortList = QuickSort(b,0,7)
print(sortList)
