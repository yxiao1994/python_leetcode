class Solution(object):
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
