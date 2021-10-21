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
            if dic[num] > targetFreq:
                res.append(num)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/231186431/

33 / 82 个通过测试用例
状态：解答错误

输入：
[2,2]
输出：
[2,2]
预期结果：
[2]
"""
