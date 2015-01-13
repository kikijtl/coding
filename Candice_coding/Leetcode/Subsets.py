'''Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]'''

from copy import deepcopy
def subsets(S):
    cur_result = []
    results = []
    #tb = {}
    for k in range(1, len(S)+1):
        subsets_dfs(S, cur_result, results, 0, k)
    results.append([])
    return results
     
def subsets_dfs(S, cur_result, results, idx, k):
    #k is the target number of length of subsets
    if len(cur_result) == k:
        if not results or cur_result != results[-1]:
            #tb[tuple(cur_result)] = 1
            results.append(deepcopy(cur_result))
        return
    for num in S[idx:]:
        cur_result.append(num)
        subsets_dfs(S, cur_result, results, S.index(num)+1, k)
        cur_result.pop()
            

if __name__ == '__main__':
    S = [1,2,3,4,5,6,7,8,9,10,0]
    print subsets(S)