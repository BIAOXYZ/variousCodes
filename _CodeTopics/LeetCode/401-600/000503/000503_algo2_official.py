class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 参考官方答案。相比trivial的O(n^2)的实现，由于每个元素入栈出栈加起来最多4次，所以整个算法是O(n)的。

        if not nums:
            return []
        
        length = len(nums)
        res = [-1 for i in range(length)]
        stk = []

        for i in range(length*2):
            while stk and nums[stk[-1]] < nums[i % length]:
                res[stk.pop()] = nums[i % length]
            stk.append(i % length)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/151587993/

224 / 224 个通过测试用例
状态：通过
执行用时: 208 ms
内存消耗: 15.2 MB

执行用时：208 ms, 在所有 Python 提交中击败了51.50%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了21.50%的用户
"""
