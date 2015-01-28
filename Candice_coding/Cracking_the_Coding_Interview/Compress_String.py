'''Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the compressed string would not become smaller than the original string, your method should return the original string.'''

def compressString(S):
    if len(S) <= 2:
        return S
    short = 0
    result = [S[0]]
    tmp = 1
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            tmp += 1
        else:
            result.append(str(tmp))
            result.append(S[i])
            short += tmp-2
            tmp = 1
    result.append(str(tmp))
    short += tmp-2    
    if short > 0:
        return ''.join(result)
    else:
        return S
    
if __name__ == '__main__':
    S_set = ['aabcccccaaa', 'abcd', 'aabbcc','abbbcccdd']
    for S in S_set:
        print compressString(S)