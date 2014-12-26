'''Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".'''

def simplifyPath(path):
    i = 0
    stack = []
    while i < len(path):
        if path[i] == '/':
            i += 1
            continue
        j = i + 1
        while j < len(path) and path[j] != '/':
            j += 1
            
        '''we extract the string between two slashes'''
        nm = path[i:j]
        if nm == '..':
            if stack:
                stack.pop()
        elif nm and nm != '.':
            stack.append(nm)
        i = j
    if len(stack) == 0:
        return '/'
    result = ''
    for k in range(len(stack)):
        result = result + '/' + stack[k]
    return result

if __name__ == '__main__':
    test_cases = ['/..', '/home//', '/a/./../../../bed/course']
    for path in test_cases:
        print path, simplifyPath(path)