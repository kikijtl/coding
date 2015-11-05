'''
Given an positive integer number n,
find all the prime factors of it.
'''

def primeFactors(n):
    if n < 3:
        return [n]
    f = 2
    factors = []
    while f * f <= n:
        while n % f == 0:
            n /= f
            factors.append(f)
        f += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == '__main__':
    ns = [91235, 128782, 192938, 4781, 7382, 615, 24242424, 3335555, 121]
    for n in ns:
        print primeFactors(n)