class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        tmp = self.pop()
        self.stack2.append(tmp)
        return tmp
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    print q.peek()