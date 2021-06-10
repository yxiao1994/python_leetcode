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


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        栈的压入弹出序列
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

    def isValid(self, s):
        """
        判断是否有效的括号
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top_ch = stack[-1]
                if ch == ')':
                    if top_ch == '(':
                        stack.pop()
                    else:
                        return False
                if ch == ']':
                    if top_ch == '[':
                        stack.pop()
                    else:
                        return False
                if ch == '}':
                    if top_ch == '{':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
