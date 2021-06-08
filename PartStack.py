class CQueue(object):
    # 两个栈实现队列

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value):
        self.s1.append(value)

    def deleteHead(self):
        if not self.s1 and not self.s2:
            return -1
        if not self.s2:
            while self.s1:
                temp = self.s1.pop()
                self.s2.append(temp)
        val = self.s2.pop()
        return val


class MinStack(object):
    # 包含最小元素的栈
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B or x <= self.B[-1]:
            self.B.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.A.pop()
        if x == self.B[-1]:
            self.B.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.B[-1]
