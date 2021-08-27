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
            return (self.lis[length/2] + self.lis[length/2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
https://leetcode-cn.com/submissions/detail/212002081/

3 / 21 个通过测试用例
状态：解答错误

最后执行的输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：
[null,null,null,1.00000,null,2.00000]
预期结果：
[null,null,null,1.5,null,2.0]
"""
