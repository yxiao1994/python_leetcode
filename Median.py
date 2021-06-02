import heapq


class MedianFinder(object):
    # 数据流中的中位数
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == 0 or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) < len(self.min_heap):
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        if len(self.max_heap) - len(self.min_heap) >= 2:
            x = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -x)

    def findMedian(self):
        """
        :rtype: float
        """
        count = len(self.min_heap) + len(self.max_heap)
        if count % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == "__main__":
    obj = MedianFinder()
    print(obj.addNum(1))
    print(obj.addNum(2))
    print(obj.findMedian())
    print((obj.addNum(3)))
    print(obj.findMedian())
