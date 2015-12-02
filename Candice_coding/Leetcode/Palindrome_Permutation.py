# Given a string, determine if a permutation of the string could form a palindrome.
# 
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
# 
# Hint:
# 
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myset = sets.Set([])
        for char in s:
            if char not in myset:
                myset.add(char)
            else:
                myset.remove(char)
        if len(s) % 2 == 0 and not myset:
            return True
        elif len(s) % 2 != 0 and len(myset) == 1:
            return True
        else:
            return False
            