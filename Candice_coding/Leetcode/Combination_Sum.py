'''Combination Sum II:
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination must be in non-descending order.
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] '''

from copy import deepcopy
def combinationSum2(candidates, target):
    cd = sorted(candidates)
    cur_re = []
    results = []
    dfs(cd, target, cur_re, results, 0)
    return results
       
def dfs(cd, tg, cur_re, results, idx):
    if tg == 0:
        results.append(deepcopy(cur_re))
        return
    if tg < 0 or idx >= len(cd):
        return
    
    cur_re.append(cd[idx])
    dfs(cd, tg-cd[idx], cur_re, results, idx+1)
    cur_re.pop()
    dfs(cd, tg, cur_re, results, idx+1)
    '''
    i = idx
    for num in cd[idx:]:
        cur_re.append(num)
        dfs(cd, tg-num, cur_re, results, i+1)
        cur_re.pop()
        i += 1
    #This method contains overlapping problems.
    '''
    

if __name__ == '__main__':
    candidates = [32,8,33,6,30,11,24,7,18,29,6,12,34,20,23,6,6,17,15,
                 9,12,6,15,21,28,31,14,26,18,33,28,15,7,18,8,32,16,19,
                 27,30,14,28,29,13,5,17,6,6,29,16,32,28]
    target = 22
    print combinationSum2(candidates, target)
    