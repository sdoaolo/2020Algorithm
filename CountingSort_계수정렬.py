#계수정렬
#인덱스 불일치로 인한 계수 개념 파괴 방지를 위해 배열을 1칸씩 늘려서 만들었다.

def countingSort(A,n,k):
    C = [0] * (k+1) 
    B = [0] * (len(A)+1) # sortedArr

    for i in range(0,k+1): #인덱스 0부터 k까지 0은 안쓸거, 1~ k 만 씀.
        C[i] = 0 #0으로 초기화
    for j in range(0,n+1): #0부터 n까지, A[0]부터 A[n]  0번 인덱스부터 마지막 인덱스까지 접근,  n은 마지막 인덱스
        C[A[j]]+=1
    for i in range(2,k+1): #2번 인덱스부터 ㅇㅇ 
        C[i] = C[i]+C[i-1]
    for j in range(n,-1,-1): 
        B[C[A[j]]] = A[j]
        C[A[j]]-=1
    return B

b= [2,2,2,1,1,3,5,5,4,5]
sortList = countingSort(b,9,5)
print(b,"\n")
print(sortList[1:len(b)+1])

