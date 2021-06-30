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

    def largestRectangleArea(self, heights):
        """
        柱状图中最大的矩形
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        left, right = [0] * n, [0] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else - 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        max_area = 0
        for i in range(n):
            max_area = max(max_area, (right[i] - left[i] - 1) * heights[i])
        return max_area

    def calculate(s):
        """
        字符串加减乘除
        :type s: str
        :rtype: int
        """
        n = len(s)
        stack = []
        sign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + int(s[i])
            if i == n - 1 or s[i] in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
        return sum(stack)
