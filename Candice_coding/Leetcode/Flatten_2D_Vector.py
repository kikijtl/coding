# Implement an iterator to flatten a 2d vector.
# 
# For example,
# Given 2d vector =
# 
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, 
# the order of elements returned by next should be: [1,2,3,4,5,6].

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vector = vec2d
        self.x = 0
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        while self.x < len(self.vector) and len(self.vector[self.x]) == 0:
            self.x += 1
        ret = self.vector[self.x][self.y]
        if self.y == len(self.vector[self.x]) - 1:
            self.x += 1
            self.y = 0
        else:
            self.y += 1
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.x < len(self.vector):
            for i in xrange(self.x, len(self.vector)):
                if len(self.vector[i]) > 0:
                    return True
        return False


if __name__ == '__main__':
    vec2d = [[], [3]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): 
        v.append(i.next())
    print v
