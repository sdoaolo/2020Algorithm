#버블 정렬, n : 배열의 마지막 인덱스

def bubbleSort(A, n):
	for last in range(n,0,-1):
		sorted = True
		for i in range(0,last):
			if A[i] > A[i+1]:
				A[i],A[i+1] = A[i+1] , A[i]
				sorted = False
		if sorted==True:
			return A
a = [3,1,8,6,10,2,4,9,7,5]
b= [2,3,8,6,9,10,7,5,1,4]
sortList = bubbleSort(b,9)

print(sortList)
