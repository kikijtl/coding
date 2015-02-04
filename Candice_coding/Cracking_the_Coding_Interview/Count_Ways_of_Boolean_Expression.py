'''Given a boolean expression consisting of the symbols 0, 1, &, | and ^,
and a desired boolean result value result, implement a function to count 
the number of ways of parenthesizing the expression such that it evaluates to result.
P335'''
'''Operator ^: 1^0=True; 0^1=True; 1^1=False; 0^0=False''' 

def countWays(exp, result, start, end, tb):
    key = (exp[start:end+1], str(result))
    if key in tb:
        '''tb is used to store the ways that exp can be result'''
        return tb[key]
    if start == end:
        if result == True and exp[start] == '1':
            return 1
        elif result == False and exp[start] == '0':
            return 1
        else:
            return 0
    count = 0
    if result == True:
        for i in range(start+1, end, 2):
            op = exp[i]
            if op == '&':
                count += countWays(exp, True, start, i-1, tb)*countWays(exp, True, i+1, end, tb)
            elif op == '|':
                count += countWays(exp, True, start, i-1, tb)*countWays(exp, True, i+1, end, tb)
                count += countWays(exp, True, start, i-1, tb)*countWays(exp, False, i+1, end, tb)
                count += countWays(exp, False, start, i-1, tb)*countWays(exp, True, i+1, end, tb)
            else:
                count += countWays(exp, True, start, i-1, tb)*countWays(exp, False, i+1, end, tb)
                count += countWays(exp, False, start, i-1, tb)*countWays(exp, True, i+1, end, tb)
    else:
        for i in range(start+1, end, 2):
            op = exp[i]
            if op == '&':
                count += countWays(exp, True, start, i-1, tb)*countWays(exp, False, i+1, end, tb)
                count += countWays(exp, False, start, i-1, tb)*countWays(exp, True, i+1, end, tb)
                count += countWays(exp, False, start, i-1, tb)*countWays(exp, False, i+1, end, tb)
            elif op == '|':
                count += countWays(exp, False, start, i-1, tb)*countWays(exp, False, i+1, end, tb)
            else:
                count += countWays(exp, False, start, i-1, tb)*countWays(exp, False, i+1, end, tb)
                count += countWays(exp, True, start, i-1, tb)*countWays(exp, True, i+1, end, tb)
    tb[key] = count
    return count


if __name__ == '__main__':
    exp = '1^0&1^0'
    result = False
    tb = {}
    n = len(exp)
    print countWays(exp, result, 0, n-1, tb)