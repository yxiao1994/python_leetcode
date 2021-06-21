class Solution(object):
    def minDistance(self, word1, word2):
        """
        字符串编辑距离
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m * n == 0:
            return max(m, n)
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(1, m + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]

    def longestPalindrome(self, s):
        """
        最长回文子串
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ''
        dp = [[False for _ in range(n)] for _ in range(n)]
        for k in range(0, n):
            for i in range(0, n - k):
                j = i + k
                if k == 0:
                    dp[i][i] = True
                elif k == 1:
                    dp[i][i + 1] = (s[i] == s[i + 1])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and k + 1 > len(res):
                    res = s[i:j + 1]
        return res

    def maxProduct(self, nums):
        """
        子数组最大乘积
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_dp, min_dp, res = nums[0], nums[0], nums[0]
        for i in range(1, n):
            temp = max(max_dp * nums[i], min_dp * nums[i], nums[i])
            min_dp = min(max_dp * nums[i], min_dp * nums[i], nums[i])
            max_dp = temp
            res = max(res, max_dp)
        return res

    def wordBreak(self, s, wordDict):
        """
        单词拆分
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(n + 1):
            for j in range(0, i):
                dp[i] = dp[j] and (s[j: i] in wordDict)
                if dp[i]:
                    break
        return dp[n]

    def minimumTotal(self, triangle):
        """
        三角形最小路径和
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)

    def lengthOfLIS(self, nums):
        """
        最长递增子序列
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def longestValidParentheses(self, s):
        """
        最长有效括号子串
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] + 2) if i > 1 else 2
                else:
                    k = i - dp[i - 1] - 1
                    if k >= 0 and s[k] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[k - 1] if k >= 1 else 0)
        return max(dp)

    def longestCommonSubsequence(self, text1, text2):
        """
        最长公共子序列
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]

    def coinChange(self, coins, amount):
        """
        硬币兑换
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

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

    def nthUglyNumber(self, n):
        """
        第n个丑数，三个指针分别记录有资格同i相乘的最小丑数位置
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]

    def maximalSquare(self, matrix):
        """
        矩阵中只包含 '1' 的最大正方形面积
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res * res

    def rob(self, nums):
        """
        打家劫舍
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

    def rob_in_tree(self, root):
        """
        二叉树中的打家劫舍
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0, 0
            l = dfs(root.left)
            r = dfs(root.right)
            selected = root.val + l[0] + r[0]
            not_selected = max(l) + max(r)
            return not_selected, selected

        res = dfs(root)
        return max(res)


if __name__ == "__main__":
    obj = Solution()
    print(obj.cuttingRope(20))
