'''
Given a number n, find all prime numbers that are less than or equal to n.
'''
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


from sets import Set
def primeNumbers(n):
    results = []
    skip = Set([])
    d = 2
    while d <= n:
        if d not in skip:
            results.append(d)
            i = 2
            while d * i <= n:
                skip.add(d*i)
                i += 1
        d += 1
    return results


if __name__ == '__main__':
    n = 120
    print primeNumbers(n)