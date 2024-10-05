class MinStack(object):
    def __init__(self):
        self.element = []
        self.minStack = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.element.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
    def pop(self):
        """
        :rtype: None
        """
        if self.element:
            top = self.element.pop()
            if top == self.minStack[-1]:
                self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.element:
            return self.element[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]