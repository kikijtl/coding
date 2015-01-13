'''Roman to Integer:
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.'''

def romanToInt(s):
    table = {}
    ch = ['I','V','X','L','C','D','M']
    dgt = [1,5,10,50,100,500,1000]
    for i in range(len(ch)):
        table[ch[i]] = dgt[i]
    if len(s) == 1:
        return table[s]
    num = 0
    for j in range(1, len(s)):
        if table[s[j]] > table[s[j-1]]:
            num = num - table[s[j-1]]
        else:
            num = num + table[s[j-1]]
    num += table[s[len(s)-1]]
    return num

'''Integer to Roman:
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
The rules of Roman can be found on wikipedia.'''




if __name__ == '__main__':
    s = 'DCXXI'
    print romanToInt(s)

