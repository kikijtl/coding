'''Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.'''

def lengthOfLongestSubstring(s):
    b = 0
    e = 0
    l = 0
    table = {}
    while e < len(s):
        if s[e] not in table:
            table[s[e]] = 1
            e += 1
        else:
            l = max(l, e-b)
            while s[b] != s[e]:
                del table[s[b]]
                b+= 1
            b += 1
            e += 1
    return max(l, e-b)

if __name__ == '__main__':
    test_case = ['qopubjguxhxdipfzwswybgfylqvjzhar']
    for s in test_case:
        print lengthOfLongestSubstring(s)