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
