'''Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.'''

def findMin(num):
    return findMinAux(num, 0, len(num)-1)
       
def findMinAux(num, s, e):
    if s == e or num[s] < num[e]:
        return num[s]
    m = s + (e-s)/2
    if num[m] <= num[e]:
        return findMinAux(num, s, m)
    if m == s or num[m] > num[s]:
        return findMinAux(num, m+1, e)
    
def findMin_iter(num):
    s = 0
    e = len(num)-1
    while s != e and num[s] >= num[e]:
        m = s + (e-s)/2
        if m == s or num[m] > num[s]:
            s = m+1
        else:
            s += 1
            e = m
    return num[s]
    
'''Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.'''

def findMin2(num):
    s = 0
    e = len(num)-1
    while s < e and num[s] >= num[e]:
        m = s + (e-s)/2
        if num[m] > num[s]:
            s = m+1
        elif num[m] < num[e]:
            s += 1
            e = m
        else:
            s += 1
    return num[s]
            

if __name__ == '__main__':
    num = [4,4,4,4,1,1,1,2,2,2,3,3,3,4,4,4]
    print findMin2(num)
            