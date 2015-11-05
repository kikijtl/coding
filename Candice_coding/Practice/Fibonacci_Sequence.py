'''
Output the nth number in the Fibonacci Sequence.
'''

def nthFibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return nthFibonacci_recursive(n-1) + nthFibonacci_recursive(n-2)

def nthFibonacci_loop(n):
    if n == 1 or n == 2:
        return 1
    previous = 1
    current = 1
    for i in xrange(3, n+1):
        tmp = current + previous
        previous = current
        current = tmp
    return current


if __name__ == '__main__':
    n = 10
    for n in xrange(1, 30):
        a = nthFibonacci_loop(n)
        b = nthFibonacci_recursive(n)
        print a, b 
        assert a == b