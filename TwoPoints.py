from collections import defaultdict


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

    def maxArea(self, height):
        """
        盛水最多的容器
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        res = 0
        i = 0
        j = n - 1
        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j - i)
                res = max(area, res)
                i += 1
            else:
                area = height[j] * (j - i)
                res = max(area, res)
                j -= 1
        return res

    def threeSum(self, nums):
        """
        三数之和
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n == 0:
            return res
        nums = sorted(nums)
        for i in range(0, n - 1):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            target = -nums[i]
            while left < right:
                twosum = nums[left] + nums[right]
                if twosum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
                    while right > left and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
                elif twosum > target:
                    right -= 1
                else:
                    left += 1
        return res

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = float('inf')
        nums = sorted(nums)
        n = len(nums)
        res = 0
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            temp_target = target - nums[i]
            while left < right:
                two_sum = nums[left] + nums[right]
                diff = two_sum - temp_target
                if diff == 0:
                    return target
                elif diff < 0:
                    left += 1
                else:
                    right -= 1
                if abs(diff) < min_diff:
                    min_diff = min(min_diff, abs(diff))
                    res = two_sum + nums[i]
        return res

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

    def minWindow(self, s, t):
        """
        最小覆盖子串
        :type s: str
        :type t: str
        :rtype: str
        """
        need_dic = defaultdict(int)
        for ch in t:
            need_dic[ch] += 1
        need_count = len(t)
        left, right = 0, 0
        res = (0, float('inf'))
        for right in range(len(s)):
            ch = s[right]
            if need_dic[ch] > 0:
                need_count -= 1
            need_dic[ch] -= 1
            if need_count == 0:
                while left < right:
                    ch = s[left]
                    if need_dic[ch] == 0:
                        break
                    need_dic[ch] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                need_dic[s[left]] += 1
                need_count += 1
                left += 1
        print(res)
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]

    def lengthOfLongestSubstring(self, s):
        """
        最长不重复子串
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        right = 0
        char_set = set()
        while left < len(s) and right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                char_set.remove(s[left])
                left += 1
        return res
