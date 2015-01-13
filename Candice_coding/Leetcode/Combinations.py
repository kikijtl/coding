from copy import deepcopy
def combine(n, k):
    cur_result = []
    results = []
    dfs(n, cur_result, results, k, 1)
    return results
      
def dfs(n, cur_result, results, k, i):
    if len(cur_result) == k:
        results.append(deepcopy(cur_result))
        return
    for j in range(i, n+1):
        cur_result.append(j)
        dfs(n, cur_result, results, k, j+1)
        cur_result.pop()
        
        
if __name__ == '__main__':
    n = 2
    k = 1
    print combine(n, k)
            