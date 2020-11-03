#선택정렬 , n:마지막 인덱

def theLargest(A,last):
	largest = 0
	for j in range(1, last+1):
		if (A[j] > A[largest]) :
			largest = j
	return largest
	
def selectionSort(A, n):
	for last in range(n,0,-1):
		k= theLargest(A,last)
		A[k],A[last] = A[last],A[k]
	return A
		
a = [3,1,8,6,10,2,4,9,7,5]
b= [2,3,8,6,9,10,7,5,1,4]
sortList = selectionSort(b,9)

print(sortList)
