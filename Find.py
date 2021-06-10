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
        旋转数组查找最小数字
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid
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


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 3, 4, 7, 9, 12]
    print(obj.lengthOfLISII([0, 1, 0, 3, 2, 3]))
