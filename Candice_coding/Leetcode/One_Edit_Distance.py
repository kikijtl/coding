'''
Time:  O(m+n)
Space: O(1)
Given two strings S and T, determine if they are both one edit distance apart.

One edit distance is defined as follow (according to WIKIPEDIA):
You can choose only one of the allowed operations:
1. insert a single character;
2. remove a single character;
3. substitute one character for another.
'''

class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m - n > 1 or n - m > 1:
            return False
        left = 0
        while left < m and left < n:
            if s[left] != t[left]:
                break
            left += 1
        if left == min(m, n):
            return True
        right = -1
        while right >= -min(m, n):
            if s[right] != t[right]:
                break
            right -= 1
        return abs(left) + abs(right) == max(m, n)


if __name__ == '__main__':
    test_cases = [('teacher', 'acher'),
                  ('teacher', 'teach'),
                  ('teacher', 'teache'),
                  ('eacher', 'teacher'),
                  ('eacher', 'teachers'),
                  ('teacher', 'peacher'),
                  ('teacher', 'peaches'),
                  ('teacher', 'peach'),
                  ('teach', 'tech'),
                  ('teach', 'tench')]
    results = [False, False, True, True, False, True, False, False, True, True]
    i = 0
    for s, t in test_cases:
        print Solution().isOneEditDistance(s, t), results[i]
        i += 1
