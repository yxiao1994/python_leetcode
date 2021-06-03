class Solution:

    def partitionArray(self, nums, k):
        """
        划分数组
        @param nums: The integer array you should partition
        @param k: An integer
        @return: The index after partition
        """
        # write your code here
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] >= k and nums[right] < k:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] < k:
                left += 1
            if nums[right] >= k:
                right -= 1
        return left
