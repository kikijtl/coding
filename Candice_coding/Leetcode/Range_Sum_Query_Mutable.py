# Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)

# For Segment Tree, see:
# http://bookshadow.com/weblog/2015/08/13/segment-tree-set-1-sum-of-given-range/

import math

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums: return
        self.nums = nums
        self.h = int(math.ceil(math.log(len(nums), 2)) + 1)  # segmentTree Height
        self.segmentTree = [0] * (2**self.h - 1)
        self.initSegmentTree(0, len(self.nums)-1, 0)
        
    def initSegmentTree(self, start, end, i):
        if start == end:
            self.segmentTree[i] = self.nums[start]
            return self.segmentTree[i]
        mid = start + (end - start) / 2
        self.segmentTree[i] = self.initSegmentTree(start, mid, 2*i+1) \
                            + self.initSegmentTree(mid+1, end, 2*i+2)
        return self.segmentTree[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.updateSegmentTree(0, len(self.nums)-1, 0, i, diff)
    
    def updateSegmentTree(self, start, end, treeIndex, i, diff):
        if i >= start and i <= end:
            self.segmentTree[treeIndex] += diff
            if start < end:
                mid = start + (end - start) / 2
                self.updateSegmentTree(start, mid, 2*treeIndex+1, i, diff)
                self.updateSegmentTree(mid+1, end, 2*treeIndex+2, i, diff)
        return

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeSegmentTree(0, len(self.nums)-1, 0, i, j)
    
    def sumRangeSegmentTree(self, treeStart, treeEnd, treeIndex, i, j):
        if j < treeStart or i > treeEnd:
            return 0
        if i <= treeStart and j >= treeEnd:
            return self.segmentTree[treeIndex]
        treeMid = treeStart + (treeEnd - treeStart) / 2
        return self.sumRangeSegmentTree(treeStart, treeMid, 2*treeIndex+1, i, j) \
            + self.sumRangeSegmentTree(treeMid+1, treeEnd, 2*treeIndex+2, i, j)
        
if __name__ == '__main__':
    nums = [1,3,5]
    numArray = NumArray(nums)
    print numArray.segmentTree
    i, j = (0,2)
    print numArray.sumRange(i, j)
    numArray.update(1, 2)
    print numArray.segmentTree
    i, j = (0,2)
    print numArray.sumRange(i, j)
