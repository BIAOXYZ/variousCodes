class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        # print 5/3, 5//3, 5.0/3, 5.0//3
        ## 1 1 1.66666666667 1.0
        targetFreq = length / 3
        
        dic, res = {}, []
        for num in nums:
            dic[num] = dic.setdefault(num, 0) + 1
        
        for k, v in dic.items():
            if v > targetFreq:
                res.append(k)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/231186807/

82 / 82 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.7 MB

执行用时：20 ms, 在所有 Python 提交中击败了90.70%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了58.91%的用户
"""
