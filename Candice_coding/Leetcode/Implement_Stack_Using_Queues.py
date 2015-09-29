import collections

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.q1:
            while self.q1:
                tmp = self.q1.popleft()
                if self.q1: self.q2.append(tmp)
        else:
            while self.q2:
                tmp = self.q2.popleft()
                if self.q2: self.q1.append(tmp)
    

    def top(self):
        """
        :rtype: int
        """
        tmp = None
        if self.q1:
            while self.q1:
                tmp = self.q1.popleft()
                self.q2.append(tmp)
        else:
            while self.q2:
                tmp = self.q2.popleft()
                self.q1.append(tmp)
        return tmp
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.q1 or self.q2:
            return False
        return True
    

if __name__ == '__main__':
    mystack = Stack()
#     mystack.push(1)
#     mystack.push(2)
#     print mystack.top()
#     mystack.pop()
#     print mystack.top()
#     mystack.pop()
    print mystack.empty()
        