'''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.'''
def isPalindrome(s):
    if not s:
        return True
    i = 0
    j = len(s)-1
    while j > i:
        if not isValid(s[i]):
            '''to skip the non-alphanumeric characters'''
            i += 1
        elif not isValid(s[j]):
            j -= 1
        elif s[i] == s[j].upper() or s[i] == s[j].lower():
            '''in order not to be case-sensitive'''
            i += 1
            j -= 1
        else:
            return False
    '''When the while loop ends, i=j, s[i]=s[j] is definitely true.'''
    return True

def isValid(ch):
        return 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'

if __name__ == '__main__':
    s = "race a car"
    print isPalindrome(s)