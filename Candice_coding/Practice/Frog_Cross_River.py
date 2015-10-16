'''
A frog wants to cross the river. The distance from the start point (0)
to the other side of the river bank is X, but the frog can only jump at
most D distance. Luckily, there will be leaves falling from trees. The
array A is the time and position of the falling leaves. A[k] means at
second k, there will be a leaf falling at position A[k]. Please find the
earliest time the frog can cross the river. If it is impossible for the
frog to cross the river, return -1. If X = 1, D = 2, you should return 0.
e.g. A = [1, 3, 1, 4, 2, 5], X = 7, D = 3.
The earliest time for the frog to cross the river is 3, because at time 3,
the frog can jump onto the leaf at position 4 and then jump to the bank.
Note: Once the leaves fall onto the river, they will not disappear.
It takes 0 seconds for the frog to jump.
D is an int between [1, 100000], X is an int between [1, 100000].
The length of array A (N) is an int between [0, 100000].
The value of A[k] is an int between [1, X-1].
The time complexity should be no more than O(N).
The space complexity should be no more than O(X).
'''




    
def solution(A, X, D):
    # This solution has not yet been proved to be right.
    if A[0] + D >= X: return 0
    if max(A) + D < X: return -1
    if min(A) > D: return -1
    leaves = [float('inf')] * X
    for i in xrange(len(A)):
        pos = A[i]
        leaves[pos] = min(leaves[pos], i)
    jump = D
    end = D
    while end < X:
        if leaves[end] < float('inf'):
            leaves[end] = max(leaves[end-D: end])
        end += 1
    ans = min(leaves[X-D: X])
    if ans < float('inf'): return ans
    return -1


if __name__ == '__main__':
    A = [1, 3, 1, 4, 2, 5]
    X = 7
    D = 3
    print solution(A, X, D)