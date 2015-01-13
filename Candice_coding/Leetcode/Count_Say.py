'''The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.'''

from copy import deepcopy
def countAndSay(n):
    string = ['1']
    for i in range(1, n):
        tmp = []
        prev = 0
        count = 1
        for curr in range(1, len(string)):
            if string[prev] == string[curr]:
                count += 1
            else:
                tmp.extend([str(count), string[prev]])
                prev = curr
                count = 1
        tmp.extend([str(count), string[prev]])
        string = deepcopy(tmp)
    string = ''.join(string)
    return string
    

if __name__ == '__main__':
    test_case = [1,2,3,4,5,6,7,8]
    for n in test_case:
        print countAndSay(n)
