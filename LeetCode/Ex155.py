class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        #if x < self.min
        
    def pop(self):
        """
        :rtype: void
        """
        self.data.pop(-1)
        
    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()


