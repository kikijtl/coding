'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.'''

def isValid(s):
    stack = []
    n = len(s)
    for i in range(n):
        #if s[i]=='(' or s[i]=='[' or s[i]=='{':
        if s[i] in ['(', '[', '{']:
            stack.append(s[i])
        elif not stack:
            return False
        elif (stack.pop(), s[i]) in [('(',')'),('[',']'),('{','}')]:
            continue
            '''
        elif s[i] == ')' and stack.pop() == '(':
            continue
        elif s[i] == ']' and stack.pop() == '[':
            continue
        elif s[i] == '}' and stack.pop() == '{':
            continue
            '''
        else:
            return False
    #print stack
    if stack:
        return False
    return True

if __name__ == '__main__':
    s = '()'
    print isValid(s)