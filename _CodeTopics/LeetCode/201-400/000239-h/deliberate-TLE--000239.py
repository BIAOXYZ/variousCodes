class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 先来个暴力，做好超时的准备了。

        res = []
        length = len(nums)
        for i in range(length-k+1):
            res.append(max(nums[i:i+k]))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/135306064/

49 / 60 个通过测试用例
状态：超出时间限制
"""
