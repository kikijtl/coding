''' Jump Game II:
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

def jump(A):
    ms = [0]*len(A) #ms[i] is Minimum step needed to reach idex i
    for i in range(1, len(A)):
        tmp = float('inf')
        for j in range(i):
            if A[j] + j >= i:
                '''this means i can be reached from j'''
                tmp = min(tmp, ms[j] + 1)
                ms[i] = tmp
    return ms[len(A)-1]

def jump_g(A):    
    ret = 0
    last = 0
    curr = 0
    for i in range(len(A)):
        if i > last:
            last = curr
            ret += 1
        curr = max(curr, i+A[i])
    return ret
                
                
if __name__ == '__main__':
    A = [1,2,3,1,1,1]
    print jump_g(A)