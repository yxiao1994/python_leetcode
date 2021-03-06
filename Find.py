# coding:utf-8
#
# Copyright 2019 Tencent Inc.
# Author: Yang Xiao(mlhustxiao@tecent.com)
#


class Solution(object):
    def search(self, nums, target):
        """
        二分查找
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def searchClosest(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid
            else:
                high = mid
        if abs(nums[low] - target) > abs(nums[high] - target):
            return high
        return low

    def kClosestNumbers(self, A, target, k):
        # write your code here
        # 排序数组中找到最接近target的k个数
        res = []
        if k == 0:
            return res
        index = self.searchClosest(A, target)
        res.append(A[index])
        low = index - 1
        high = index + 1
        while len(res) < k:
            diff1 = abs(A[low] - target) if low >= 0 else float('inf')
            diff2 = abs(A[high] - target) if high < len(A) else float('inf')
            if diff1 <= diff2:
                res.append(A[low])
                low -= 1
            else:
                res.append(A[high])
                high += 1
        return res

    def searchRange(self, nums, target):
        """
        二分查找包含重复元素
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。
        找出给定目标值在数组中的开始位置和结束位置。
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                while low < high and nums[low] != target:
                    low += 1
                while low < high and nums[high] != target:
                    high -= 1
                res = [low, high]
                return res
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        res = [-1, -1]
        return res

    def RotateSearch(self, nums, target):
        """
        旋转数组查找
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    def findMin(self, nums):
        """
        旋转数组最小数字
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] == nums[high]:
                x = float('inf')
                for i in range(low, high + 1):
                    x = min(x, nums[i])
                return x
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return min(nums[low], nums[high])

    def kthLargestElement(self, n, nums):
        """
        寻找数组中第n大的元素
        :param n:
        :param nums:
        :return:
        """

        def partition(nums, p, r):
            i = p - 1
            for j in range(p, r):
                if nums[j] < nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def kthminElement(n, nums, p, r):
            # write your code here
            q = partition(nums, p, r)
            k = q - p + 1
            if k == n:
                return nums[q]
            elif k < n:
                return kthminElement(n - k, nums, q + 1, r)
            else:
                return kthminElement(n, nums, p, q - 1)

        n = len(nums) - n + 1
        return kthminElement(n, nums, 0, len(nums) - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        寻找两个正序数组的中位数
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findkth(nums1, start1, nums2, start2, k):
            if start1 >= len(nums1):
                return nums2[start2 + k - 1]
            if start2 >= len(nums2):
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            index1 = start1 + k // 2 - 1
            index2 = start2 + k // 2 - 1
            val1 = nums1[index1] if index1 < len(nums1) else float('inf')
            val2 = nums2[index2] if index2 < len(nums2) else float('inf')
            if val1 < val2:
                return findkth(nums1, index1 + 1, nums2, start2, k - k // 2)
            else:
                return findkth(nums1, start1, nums2, index2 + 1, k - k // 2)

        m, n = len(nums1), len(nums2)
        if ((m + n) % 2) == 1:
            return findkth(nums1, 0, nums2, 0, (m + n + 1) // 2)
        else:
            return (findkth(nums1, 0, nums2, 0, (m + n) // 2) + findkth(nums1, 0, nums2, 0, (m + n) // 2 + 1)) * 0.5

    def findPeakElement(self, nums):
        """
        寻找峰值
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 3, 4, 7, 9, 12]
    print(obj.lengthOfLISII([0, 1, 0, 3, 2, 3]))
