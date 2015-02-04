'''A circus is designing a tower routine consisting of people standing atop one
another's shoulders. For practical and aesthetic reasons, each person must be both shorter 
and lighter than the person below him or her. Given the heights and weights of each person 
in the circus, write a method to compute the largest possible number of people in such a tower.'''

'''We have an array. Assume the index is the height of each person, and A[i] is the weight of that person.'''

def longestIncrease(A):
    count = [1]*len(A)
    max_c = 1
    for i in range(1, len(A)):
        sub_c = -float('inf')
        for j in range(0, i):
            if A[i] > A[j]:
                sub_c = max(sub_c, count[j]+1)
        count[i] = max(sub_c, count[i])
        max_c = max(max_c, count[i])
    return max_c


if __name__ == '__main__':
    A = [3,2,5,7,6,1,9]
    print longestIncrease(A)