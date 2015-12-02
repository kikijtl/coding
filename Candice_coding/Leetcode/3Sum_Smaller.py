# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# 
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# 
# Return 2. Because there are two triplets which sums are less than 2:
# 
# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        k = 0
        count = 0
        while k < len(nums)-2:
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j - i
                    i += 1
            k += 1
        return count
                