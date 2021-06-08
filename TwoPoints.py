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

    def spiralOrder(self, matrix):
        """
        顺时针打印矩阵/螺旋打印矩阵
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if left <= right and top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

    def lengthOfLongestSubstring(self, s):
        """
        最长不重复子串
        :type s: str
        :rtype: int
        """
        char_set = set()
        j = 0
        i = 0
        res = 0
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                if res < j - i:
                    res = j - i
            else:
                char_set.remove(s[i])
                i += 1
        return res