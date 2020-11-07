def Select(A,p,r,i): #i번째 작은 원소를 찾는다. 
    if(p==r):
        return A[p]
    q = partition(A,p,r)
    k = q - p +1

    if(i<k) :
        return Select(A,p,q-1,i)
    elif i ==k:
        return A[q]
    else:
        return Select(A,q+1,r,i-k)

	
def partition(A,p,r):
	x = A[r]
	i = p-1
	for k in range(p,r+1): 
		# p to r
		if (A[k] < x and k != r) :
			if (i+1 == r) : 
				i+=1
			i+=1
			A[i],A[k] = A[k],A[i]
	A[i+1],A[r] = A[r],A[i+1]
	return i+1


a= [22,44,66,88,111] 
#b= [3,6,2,4,1,8,7,5]
#findValue = Select(b,0,7,5)
findValue = Select(a,0,4,3)
print(findValue)
