import heapq


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
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


if __name__ == "__main__":
    obj = Solution()
    print(obj.getLeastNumbers([1, 3, 4, 5, 6, 7], 2))
