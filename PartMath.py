import math


class Solution(object):
    def reverse(self, x):
        """
        整数翻转
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            res = (res * 10 + x % 10)
            if res > math.pow(2, 31) - 1:
                return 0
            x = (x // 10)
        res = res * sign
        return res

    def myAtoi(self, s):
        """
        字符串转整数
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        res = 0
        sign = 1
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0

        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1
            i += 1

        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                res = res * 10 + int(s[i])
                if res > math.pow(2, 31):
                    break
            else:
                break
            i += 1
        res *= sign
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res

    def hammingWeight(self, n):
        """
        二进制中1的个数
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += 1
            n &= (n - 1)
        return res

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def pow(x, n):
            if n == 0:
                return 1
            k = n // 2
            v = pow(x, k)
            if n & 1 == 1:
                return v * v * x
            else:
                return v * v

        if n >= 0:
            return pow(x, n)
        else:
            return 1.0 / pow(x, -n)

    def merge(self, intervals):
        """
        合并区间
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if not intervals:
            return res
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            temp = intervals[i]
            if temp[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], temp[1])
            else:
                res.append(temp)
        return res

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left = 1
        right = x - 1
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def multiply(self, num1, num2):
        """
        字符串相乘
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0 for _ in range(m + n)]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1[i]) * int(num2[j])
        carry = 0
        for i in range(m + n):
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
        if res[-1] == 0:
            res = res[:-1]
        res = res[::-1]
        return ''.join([str(x) for x in res])
