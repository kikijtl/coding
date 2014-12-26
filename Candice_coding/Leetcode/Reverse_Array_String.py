def reverse(x):
    x = str(x)
    X = list(x)
    if X[0] == '-':
        start = 1
    else:
        start = 0
    n = len(X)
    i = start
    j = n-1
    while i <= j:
        tmp = X[i]
        X[i] = X[j]
        X[j] = tmp
        i += 1
        j -= 1
    bound = 2147483647
    #bound for 32-bit integer
    result = ''.join(X)
    result = int(result)
    if result > bound or result < (-1)*bound:
        return 0
    return int(result)


def reverseWords(s):
    A = list(s)
    n = len(A)
    A = reverseStr(A, 0, n-1)
    R = []
    i = findStart(A, 0, n-1)
    while i < n:
        j = i
        while j < n and A[j] != ' ':
            j += 1
        R.extend(reverseStr(A, i, j-1))
        R.append(' ')
        i = findStart(A, j, n-1)
    ret = ''.join(R[:-1])
    return ret

def reverseStr(A, start, end):
    i = start
    j = end
    while j > i:
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp
        i += 1
        j -= 1
    return A[start:end+1]

def findStart(A, start, end):
    while start <= end and A[start] == ' ':
        start += 1
    return start


if __name__ == '__main__':
    x = 100
    print reverse(x)
    s = ''
    print reverseWords(s)