class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        indices = range(len(nums))
        res = []

        def backtrace(currArr, leftArr):
            if not leftArr:
                elem = []
                for i in currArr:
                    elem.append(nums[i])
                if elem not in res:
                    res.append(elem)
                return
            for ind, num in enumerate(leftArr):
                currArr.append(num)
                leftArr.remove(num)
                backtrace(currArr, leftArr)
                currArr.remove(num)
                leftArr.insert(ind, num)

        backtrace([], indices)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109345766/

30 / 30 个通过测试用例
状态：通过
执行用时: 1124 ms
内存消耗: 12.6 MB

执行用时：1124 ms, 在所有 Python 提交中击败了6.39%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了60.27%的用户
"""
