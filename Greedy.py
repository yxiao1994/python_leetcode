class Solution(object):
    def canJump(self, nums):
        """
        跳跃游戏
        :type nums: List[int]
        :rtype: bool
        """
        max_step = 0
        n = len(nums)
        for i in range(n):
            if i <= max_step:
                max_step = max(max_step, nums[i] + i)
        return max_step >= n - 1

    def jump(self, nums):
        """
        跳跃游戏II
        :type nums: List[int]
        :rtype: int
        """
        max_step = 0
        n = len(nums)
        res = 0
        end = 0
        for i in range(n - 1):
            if i <= max_step:
                max_step = max(max_step, nums[i] + i)
                if i == end:
                    end = max_step
                    res += 1

        return res

    def lengthOfLISII(self, nums):
        """
        最长递增子序列,n*log(n)版本
        dp记录长度为i的LIS的末尾元素的最小值
        :param nums:
        :return:
        """
        dp = []
        n = len(nums)
        if n == 0:
            return 0
        dp.append(nums[0])
        for i in range(n):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                l, r = 0, len(dp) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if nums[i] > dp[mid]:
                        l = mid + 1
                    else:
                        loc = mid
                        r = mid - 1
                dp[loc] = nums[i]
        return len(dp)

