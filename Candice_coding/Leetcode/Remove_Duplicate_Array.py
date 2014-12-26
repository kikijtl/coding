def removeDuplicates(A):
    n = len(A)
    if n == 0:
        return n
    i = 0
    j = 0
    while i < n and j < n:
        if A[j] == A[i]:
            j += 1
        else:
            i += 1
            A[i] = A[j]
    #return the length of array
    return i+1

def removeDuplicates2(A):
    n = len(A)
    if n <= 1:
        return n
    i = 0
    j = 1
    count = 0
    while i < n and j < n:
        if A[j] == A[i]:
           count += 1
           A[i+1] = A[j]
           j += 1
        elif count > 0:
            i += 2
            A[i] = A[j]
            j += 1
            count = 0
        else:
            i += 1
            A[i] = A[j]
            j += 1
    if count > 0:
        return i+2
    else:
        return i+1
    
def removeElement(A, elem):
    n = len(A)
    if n == 0:
        return n
    i = 0
    j = n-1
    while i < n and j > i:
        if A[i] != elem:
            i += 1
            continue
        if A[j] == elem:
            j -= 1
            continue
        A[i] = A[j]
        i += 1
        j -= 1
    if j == i and A[i] != elem:
        return i+1
    else:
        return i
    

    
if __name__ == '__main__':
    A = [1,1,1,1,2,2,2,3]
    #l = removeDuplicates2(A)
    #print A[:l]
    elem = 1
    nl = removeElement(A, elem)
    print A[:nl]