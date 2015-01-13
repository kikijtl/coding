'''Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].'''

from copy import deepcopy
def permute(num):
    n = len(num)
    #count = [1] * n
    cur_result = []
    results = []
    dfs(num,cur_result, results, n)
    return results

def dfs(num, cur_result, results, n):
    if not num:
        results.append(deepcopy(cur_result))
        return
    for each_num in num:
        cur_result.append(each_num)
        idx = num.index(each_num)
        new = num[:idx] + num[idx+1:]
        dfs(new, cur_result, results, n)
        cur_result.pop()
        

if __name__ == '__main__':
    num = [0, 1]
    print permute(num)