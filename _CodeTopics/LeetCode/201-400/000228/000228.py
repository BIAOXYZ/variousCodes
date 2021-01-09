class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        res = []
        tmpSequence = []
        for i in range(len(nums)):
            if not tmpSequence or nums[i] == tmpSequence[-1] + 1:
                tmpSequence.append(nums[i])
            else:
                if len(tmpSequence) > 1:
                    res.append(str(tmpSequence[0]) + "->" + str(tmpSequence[-1]))
                else:
                    res.append(str(tmpSequence[0]))
                tmpSequence = [nums[i]]
        
        # 循环完，最后还有一个tmpSequence需要往res里贴一下。
        if len(tmpSequence) > 1:
            res.append(str(tmpSequence[0]) + "->" + str(tmpSequence[-1]))
        elif len(tmpSequence) == 1:
            res.append(str(tmpSequence[0]))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/137256617/

28 / 28 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13 MB

执行用时：12 ms, 在所有 Python 提交中击败了86.79%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了45.93%的用户
"""
