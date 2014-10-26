def counting_sort(A, max):
    '''the input is the original array A and the max number in A
       the output is the sorted of A'''
    n = len(A)
    C = []
    for i in range(max+1):
        C.append(0)
    for j in range(n):
        C[A[j]] += 1
        # This is the counting array
    for i in range(1, len(C)):
        C[i] += C[i-1]  
        # This is the index array  
    B = [0]*n
    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        # Scan A from backwards.
        # The position of A[j] in B is decided by C[A[j]]
        C[A[j]] -= 1
    return B    
        
if __name__ == '__main__':
    A = [9,2,3,6,5,6,9,1,0,3,5]
    print counting_sort(A, max(A))
        