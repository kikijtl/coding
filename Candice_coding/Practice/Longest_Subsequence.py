'''
There is an int sequence. Find the length of the longest subsequence
so that difference between the maximum number and the minimum number
in the subsequence is less than 1.
For example, the longest subsequence of [1,3,2,2,5,2,3,7] is
[3,2,2,2,3], and your function should return 5.
The space complexity should be O(n)
'''

def longestSubsequence1(array):
    '''Use Hash Table'''
    count_dict = {}
    max_num = -float('inf')
    min_num = float('inf')
    max_length = 0
    for x in array:
        max_num = max(max_num, x)
        min_num = min(min_num, x)
        if x not in count_dict:
            count_dict[x] = 1
        else:
            count_dict[x] += 1
    for i in xrange(min_num, max_num+1):
        if i not in count_dict:
            continue
        if i+1 in count_dict:
            max_length = max(max_length, count_dict[i]+count_dict[i+1])
        else:
            max_length = max(max_length, count_dict[i])
    return max_length


def longestSubsequence2(array):
    '''Use sort array'''
    array.sort()
    i, j = 0, 1
    max_length = 0
    while i <= j and j < len(array):
        if array[j] - array[i] <= 1:
            j += 1
            continue
        max_length = max(max_length, j-i)
        i += 1
    max_length = max(max_length, j-i)
    return max_length
        
    

if __name__ == '__main__':
#     array = [1,3,2,9,6,2,6,7]
#     array = [1,1,1,1,1,1,1]
#     array = [3,5,7,1,9]
    array = [9,1,3,3,7,5]
    print longestSubsequence1(array)
    print longestSubsequence2(array)
      
