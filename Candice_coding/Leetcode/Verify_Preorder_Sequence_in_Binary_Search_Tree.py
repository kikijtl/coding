# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
# 
# You may assume each number in the sequence is unique.
# 
# Follow up:
# Could you do it using only constant space complexity?


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # Use extra space
        stack = []
        tmp = float('-inf')
        for p in preorder:
            if p < tmp: 
                # if tmp != float('-inf'), which means right-side elements already show up, no more elements < root should occur
                return False
            # p is on the right side of root(tmp)
            while stack and stack[-1] < p:
                tmp = stack.pop()
                # The last element popped out is the root of current p
            stack.append(p)
        return True
        