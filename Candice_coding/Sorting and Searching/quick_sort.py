''' implement quick sort
'''

def quick_sort(A, start, end):
    if start >= end:
        return 
    pivot = A[start]
    i = 1
    for j in range(1, len(A)):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[start], A[i-1] = A[i-1], A[start]
    quick_sort(A, start, i-2)
    quick_sort(A, i , end)
    
def quick_sort_return(A):
    if len(A)==0 or len(A)==1:
        return A
    pivot = A[0]
    i = 1
    for j in range(1, len(A)):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[0], A[i-1] = A[i-1], A[0]
    left = quick_sort_return(A[:i-1])
    right = quick_sort_return(A[i:])
    return left+[A[i-1]]+right

if __name__=='__main__':
    A=[6,5,4,3,3,2,4,4,4,1,5]
    #quick_sort(A, 0, len(A)-1)
    #print A
    print quick_sort_return(A)
    