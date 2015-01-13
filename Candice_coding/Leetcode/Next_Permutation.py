def next_permutation(A):
    i = len(A)-1
    while i > 0:
        if A[i] > A[i-1]:
            break
        else:
            i-=1
    if i==0:
        return sorted(A)
    i-=1
    j = len(A)-1
    while j > i:
        if A[j] > A[i]:
            break
        else:
            j-=1
    A[i],A[j] = A[j], A[i]
    return A[:i+1]+sorted(A[i+1:])

if __name__=='__main__':
    test_cases = [[1,2,3], [4,3,1], [3,5,9,6,4], [3,6,8,2]]
    for each_test_case in test_cases:
        print each_test_case, next_permutation(each_test_case)
