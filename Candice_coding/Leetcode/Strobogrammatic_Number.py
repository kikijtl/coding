# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# 
# For example, the numbers "69", "88", and "818" are all strobogrammatic.


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        table = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        result_ls = []
        for char in num:
            if char not in table:
                return False
            result_ls.append(table[char])
        result_ls.reverse()
        return ''.join(result_ls) == num