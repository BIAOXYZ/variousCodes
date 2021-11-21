class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.d ={}
        for i, elem in enumerate(arr):
            if self.d.has_key(elem):
                self.d[elem].append(i)
            else:
                self.d[elem] = [i]

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        if value not in self.d.keys():
            return 0
        currValueInds = self.d[value]
        l = bisect.bisect_left(currValueInds, left)
        r = bisect.bisect_right(currValueInds, right)
        ##print l, r
        return r - l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

"""
https://leetcode-cn.com/submissions/detail/240720373/

20 / 20 个通过测试用例
状态：通过
执行用时: 4312 ms
内存消耗: 52.4 MB
"""
