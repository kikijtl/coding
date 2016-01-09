# Given an unsorted integer array, find the first missing positive integer.
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# Your algorithm should run in O(n) time and uses constant space.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Try to put each num in their own position-1.
        # e.g. put 1 in position 0, put 2 in position 1, ...
        # e.g. [5,6,7,8] should return 1
        # The first number that != position+1 is the first missing positive number
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[i] != i+1 \
                and nums[nums[i]-1] != nums[i]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
                # Be careful for the exchange. Must put the nums[i] to the
                # right position first. Otherwise, nums[i] will be changed
                # and nums[nums[i]-1] is not correct.
            else:
                i += 1
        for i in xrange(n):
            if nums[i] != i + 1:
                return i+1
        return n+1


if __name__ == '__main__':
    nums = [-1,3,4,1,1]
    print Solution().firstMissingPositive(nums)