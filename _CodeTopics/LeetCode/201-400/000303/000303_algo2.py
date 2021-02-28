class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 真屁事多，搞这么个条件：nums可能为空。。。关键i和j是严格小于nums.length的。
        if not nums:
            return
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
https://leetcode-cn.com/submissions/detail/149627154/

16 / 16 个通过测试用例
状态：通过
执行用时: 188 ms
内存消耗: 16.6 MB

执行用时：188 ms, 在所有 Python 提交中击败了62.60%的用户
内存消耗：16.6 MB, 在所有 Python 提交中击败了70.73%的用户
"""
