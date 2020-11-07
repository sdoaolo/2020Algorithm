def max_heapify(A, size, root):
    child = root * 2
    while child <= size:
        if child < size and A[child - 1] < A[child]:
            child += 1
        if A[root - 1] < A[child - 1]:
            A[root - 1], A[child - 1] = A[child - 1], A[root - 1]
        root = child
        child = root * 2

def HeapSort(A, size):
    # build heap
    for i in range(int(size/2), 0, -1):
        max_heapify(A, size, i)

    # 정렬 과정 
    for i in range(size, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        max_heapify(A, i - 1, 1)

    return A

a=[3,1,8,6,10,2,4,9,7,5]
b=[3,7,5,9,6,1,2,4,8,0]
sortList = HeapSort(b,10)
sortList2 = HeapSort(a,10)
print(sortList)
print(sortList2)
