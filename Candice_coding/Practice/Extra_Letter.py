# You have two strings containing the same characters where one string contains an extra character at a random index. 
# Write a function that accepts these strings and returns the extra character (may be in either one of the strings)
# Google engineering residency program

def extraLetter(s1, s2):
    i = 0
    while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
        i += 1
#     j = 1
#     while j < min(len(s1), len(s2)) and s1[len(s1)-j] == s2[len(s2)-j]:
#         j += 1
    if len(s1) > len(s2):
        return i, s1[i]
    else:
        return i, s2[i]


if __name__ == '__main__':
    tests = [('asjewr', 'asjeewr'), ('auqyqw', 'auqyqwa'), ('', 'b'), ('awe', 'aawer')]
    for s1, s2 in tests:
        print extraLetter(s1, s2)
