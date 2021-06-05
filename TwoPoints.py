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

    def closestTargetValue(self, target, array):
        # 在数组中找到两个数，使得它们的和最接近目标值但不超过目标值
        if not array or len(array) == 1:
            return -1
        nums = sorted(array)
        if nums[0] + nums[1] > target:
            return -1
        left = 0
        right = len(nums) - 1
        res = float('-inf')
        while left < right:
            temp_sum = nums[left] + nums[right]
            if temp_sum == target:
                return temp_sum
            elif temp_sum < target:
                left += 1
                res = max(res, temp_sum)
            else:
                right -= 1
        return res
