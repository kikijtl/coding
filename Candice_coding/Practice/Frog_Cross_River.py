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
    bin_num = (-X-1) / (D+1)
    bin_num = -bin_num
    bins = [[float('inf'), -float('inf')] for i in xrange(bin_num)]
    count = 0
    for i in xrange(len(A)):
        bin_index = A[i] / (D+1)
        if bins[bin_index][0] > A[i]:
            bins[bin_index][0] = A[i]
            if bin_index > 0 and bins[bin_index-1][1] + D > bins[bin_index][0]:
                count += 1
                bins[bin_index-1][1] = float('inf')
                bins[bin_index][0] = -float('inf')
        if bins[bin_index][1] < A[i]:
            bins[bin_index][1] = A[i]
            if bin_index < len(bins)-1 and bins[bin_index][1] + D > bins[bin_index+1][0]:
                count += 1
                bins[bin_index][1] = float('inf')
                bins[bin_index+1][0] = -float('inf')
        if count == bin_num - 1:
            return i
    return -1


if __name__ == '__main__':
    A = [1, 3, 1, 4, 2, 5]
    X = 7
    D = 3
    print solution(A, X, D)