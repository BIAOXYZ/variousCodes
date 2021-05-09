class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 我觉得题目用例2写错了，[2,3,3,1,2]的答案应该是20，而不是18。
        
        keys = list(set(nums))
        keys.sort()
        ctr = collections.Counter(nums)
        summ = sum(nums)
        res = 0
        
        for k in keys:
            res = max(res, k * summ)
            summ -= k * ctr[k]
        return res % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/175720004/

9 / 41 个通过测试用例
状态：解答错误

最后执行的输入：
[2,3,3,1,2]
"""
