class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lis = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.lis.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.lis)
        if length & 1 == 1:
            return self.lis[length/2]
        else:
            return (self.lis[length/2] + self.lis[length/2 - 1]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
https://leetcode-cn.com/submissions/detail/212007389/

9 / 21 个通过测试用例
状态：解答错误

最后执行的输入：
["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
输出：
[null,null,6.00000,null,8.00000,null,10.00000,null,6.00000,null,2.00000,null,4.00000,null,6.00000,null,5.50000,null,5.00000,null,2.50000,null,0.00000]
预期结果：
[null,null,6.0,null,8.0,null,6.0,null,6.0,null,6.0,null,5.5,null,6.0,null,5.5,null,5.0,null,4.0,null,3.0]
"""
