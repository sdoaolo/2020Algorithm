#삽입정렬, n: 마지막 인덱스 번호

def insertionSort(A, n):
	for i in range(1,n+1):
		newitem = A[i]
		loc = i-1
		while(loc >=0 and newitem <A[loc]):
			A[loc+1] = A[loc]
			loc=loc-1
		A[loc+1] = newitem
	return A
a = [3,1,8,6,10,2,4,9,7,5]
b= [2,3,8,6,9,10,7,5,1,4]
sortList = insertionSort(b,9)

print(sortList)
