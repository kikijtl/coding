# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# 
# Example 1:
# Given the list [[1,1],2,[1,1]],
# 
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
# 
# Example 2:
# Given the list [1,[4,[6]]],
# 
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return self.value.__repr__()
    
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.value, int)

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.value
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger():
            return None
        else:
            return self.value
        

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.stack.append([nestedList, 0])
        # The stack is used to collect all nestedList into it, 0 is the initial index

    def next(self):
        """
        :rtype: int
        """
        # Return the integer in the nestedList on the top of stack
        if self.hasNext():
            nestedList, i = self.stack[-1]
            result = nestedList[i].getInteger()
            self.stack[-1][1] += 1
            return result

    def hasNext(self):
        """
        :rtype: bool
        """
        # Pop out nestedList that has been walked through
        # Keep adding nestedList on top of stack until finding an integer
        # If the stack is empty, then return False
        while self.stack:
            nestedList, i = self.stack[-1]
            if self.stack[-1][1] >= len(self.stack[-1][0]):
                self.stack.pop()
                continue
            if nestedList[i].isInteger():
                return True
            self.stack[-1][1] += 1  # point to the next element
            self.stack.append([nestedList[i].getList(), 0])
        return False
            
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    list = [[1,1],2,[1,1]]
    int1 = NestedInteger(1)
    int2 = NestedInteger(2)
    nestedList = []
    nestedList.append(NestedInteger([int1, int1]))
    nestedList.append(int2)
    nestedList.append(NestedInteger([int1, int1]))
    print nestedList
    result = []
    i = NestedIterator(nestedList)
    while i.hasNext():
        result.append(i.next())
    print result