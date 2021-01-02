from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 这次用一个k长（k-size?不知道有没有这种学名）的单调栈来解决。
        ## --> 其实更准备的叫法是单调队列。。。
        ## 这次为了效率不用普通list，用deque了。

        res, monotoneStk = [], deque([])
        length = len(nums)
        
        for i in range(k):
            while monotoneStk and nums[i] >= nums[monotoneStk[-1]]:
                monotoneStk.pop()
            monotoneStk.append(i)
        res.append(nums[monotoneStk[0]])

        for i in range(k, length):
            # 当前栈底（也就是值最大的元素对应的index）一定是最“旧”的。所以上来先看看当前最旧的元素的index还合法不，
            # 不合法的话就pop出去。
            if monotoneStk and monotoneStk[0] < i - k + 1:
                monotoneStk.popleft()
            while monotoneStk and nums[i] >= nums[monotoneStk[-1]]:
                monotoneStk.pop()
            if len(monotoneStk) < k:
                monotoneStk.append(i)
            res.append(nums[monotoneStk[0]])

        return res
        
"""
https://leetcode-cn.com/submissions/detail/135381745/

60 / 60 个通过测试用例
状态：通过
执行用时: 368 ms
内存消耗: 28.7 MB

执行用时：368 ms, 在所有 Python 提交中击败了89.12%的用户
内存消耗：28.7 MB, 在所有 Python 提交中击败了43.35%的用户
"""
