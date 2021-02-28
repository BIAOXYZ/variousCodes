class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[-1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum[j] - self.prefixSum[i-1] if i != 0 else self.prefixSum[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
https://leetcode-cn.com/submissions/detail/149626953/

1 / 16 个通过测试用例
状态：执行出错

执行出错信息：
Line 7: IndexError: list index out of range
最后执行的输入：
["NumArray"]
[[[]]]
"""
