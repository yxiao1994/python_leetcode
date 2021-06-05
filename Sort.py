import heapq


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


if __name__ == "__main__":
    obj = Solution()
    print(obj.getLeastNumbers([1, 3, 4, 5, 6, 7], 2))
