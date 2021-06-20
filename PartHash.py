class Solution(object):
    def subarraySum(self, nums, k):
        """
        数组中和为 k 的连续的子数组的个数
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = dict()
        dic[0] = 1
        temp_sum = 0
        count = 0
        for v in nums:
            temp_sum += v
            count += dic.get(temp_sum - k, 0)
            dic[temp_sum] = dic.get(temp_sum, 0) + 1
        return count
