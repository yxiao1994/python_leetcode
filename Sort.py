import heapq
import random


class Solution(object):
    def minNumber(self, nums):
        """
        把数组排成最小的数
        :type nums: List[int]
        :rtype: str
        """

        def partition(nums, p, r):
            i = p - 1
            for j in range(p, r):
                if nums[j] + nums[r] <= nums[r] + nums[j]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quick_sort(nums, p, r):
            if p < r:
                q = partition(nums, p, r)
                quick_sort(nums, p, q - 1)
                quick_sort(nums, q + 1, r)

        nums = [str(x) for x in nums]
        quick_sort(nums, 0, len(nums) - 1)
        return ''.join(nums)

    def getLeastNumbers(self, arr, k):
        """
        数组中最小的k个数
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        res = [-x for x in arr[:k]]
        heapq.heapify(res)
        for num in arr[k:]:
            if -num > res[0]:
                heapq.heapreplace(res, -num)
        return [-x for x in res]

    def kthLargestElement(self, n, nums):
        # 第k大元素
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

    def exchange(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def BubbleSort(self, nums):
        # 冒泡排序
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def InsertionSort(self, nums):
        # 插入排序
        n = len(nums)
        for i in range(1, n):
            j = i - 1
            x = nums[i]
            while j >= 0 and nums[j] > x:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = x

    def partition(self, nums, p, r):
        i = p - 1
        for j in range(p, r):
            if nums[j] <= nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def _quick_sort(self, nums, p, r):
        if p < r:
            q = self.partition(nums, p, r)
            self._quick_sort(nums, p, q - 1)
            self._quick_sort(nums, q + 1, r)

    def QuickSort(self, nums):
        self._quick_sort(nums, 0, len(nums) - 1)

    def merge_array(self, nums, left, mid, right):
        L = nums[left: mid + 1]
        R = nums[mid + 1: right + 1]
        L.append(float('inf'))
        R.append(float('inf'))
        i, j = 0, 0
        for k in range(left, right + 1):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1

    def _merge_sort(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(nums, left, mid)
            self._merge_sort(nums, mid + 1, right)
            self.merge_array(nums, left, mid, right)

    def MergeSort(self, nums):
        # 归并排序
        self._merge_sort(nums, 0, len(nums) - 1)

    def heapify(self, nums, i, n):
        while i < n:
            child = i * 2 + 1
            if child >= n:
                break
            if child + 1 < n and nums[child] < nums[child + 1]:
                child += 1
            if nums[i] < nums[child]:
                nums[i], nums[child] = nums[child], nums[i]
                i = child
            else:
                break

    def build_heap(self, nums):
        n = len(nums)
        i = n // 2 - 1
        while i >= 0:
            self.heapify(nums, i, n)
            i -= 1

    def HeapSort(self, nums):
        # 堆排序
        self.build_heap(nums)
        i = len(nums) - 1
        while i > 0:
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)
            i -= 1

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        left_count = self.merge_sort(nums, left, mid)
        right_count = self.merge_sort(nums, mid + 1, right)
        count = 0
        L = nums[left: mid + 1]
        R = nums[mid + 1: right + 1]
        L.append(float('inf'))
        R.append(float('inf'))
        i = 0
        j = 0
        for k in range(left, right + 1):
            if L[i] <= R[j]:
                count += j
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
        return left_count + right_count + count

    def reversePairs(self, nums):
        """
        数组中的逆序对
        :type nums: List[int]
        :rtype: int
        """
        return self.merge_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    obj = Solution()
    nums = list(range(50))
    random.shuffle(nums)
    print(nums)
    obj.HeapSort(nums)
    print(nums)
