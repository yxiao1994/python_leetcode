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
