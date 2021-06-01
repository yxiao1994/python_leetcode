class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        return dp[-1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.cuttingRope(20))