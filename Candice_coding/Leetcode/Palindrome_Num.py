'''Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? No

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

def isPalindrome(x):
    if x < 0:
        return False
    n = 0
    while x % 10**n != x:
        n += 1
    while n > 1:
        if x / 10**(n-1) != x % 10:
            return False
        dig = x / 10**(n-1)
        x = (x % 10**(n-1)) / 10
        n -= 2
    return True

if __name__ == '__main__':
    test_case = [1221, 1001, 1011, 10011]
    for x in test_case:
        print x, isPalindrome(x)