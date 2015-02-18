'''Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.'''

def reverse(x):
    if x > 0:
        sign = 1
    else:
        sign = -1
    x = abs(x)
    ans = 0
    while x > 0:
        ans = ans*10 + x%10
        x /= 10
    return sign*ans

if __name__ == '__main__':
    test = [123, -123, 0, 10]
    '''for x in test:
        print reverse(x),'''
    print reverse(-321)