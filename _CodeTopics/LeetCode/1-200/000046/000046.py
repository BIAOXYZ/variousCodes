class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        res = []

        def backtrace(currArr, leftArr):
            if not leftArr:
                res.append(currArr[:])
                return
            for ind, num in enumerate(leftArr):
                currArr.append(num)
                leftArr.remove(num)
                backtrace(currArr, leftArr)
                currArr.remove(num)
                leftArr.insert(ind, num)

        backtrace([], nums)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109204863/

25 / 25 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.5 MB

执行用时：24 ms, 在所有 Python 提交中击败了63.96%的用户
内存消耗：12.5 MB, 在所有 Python 提交中击败了68.03%的用户
"""
