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
        res = 0
        for ind in self.d[value]:
            if left <= ind <= right:
                res += 1
        return res


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

"""
https://leetcode-cn.com/submissions/detail/240712797/

16 / 20 个通过测试用例
状态：超出时间限制

最后执行的输入：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
"""
