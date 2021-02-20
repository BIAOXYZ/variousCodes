class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        length = len(nums)
        left = right = 0
        # 当滑动窗口左端弹出某个值时，必须知道弹出这个值是不是最大/小值，并且如果是的话那么接下来的最大/小值
        # 是啥。所以各自只用一个变量是不够的，必须各自维持一个双元素的单调栈。
        currMaxStk = []
        currMinStk = []
        maxLen = 1

        while right < length:
            while currMaxStk and nums[currMaxStk[-1]] <= nums[right]:
                currMaxStk.pop()
            currMaxStk.append(right)
            while currMinStk and nums[currMinStk[-1]] >= nums[right]:
                currMinStk.pop()
            currMinStk.append(right)
            if abs(nums[currMaxStk[0]] - nums[currMinStk[0]]) <= limit:
                right += 1
            else:
                maxLen = max(maxLen, right - left)
                if currMaxStk[0] == left:
                    currMaxStk.pop(0)
                if currMinStk[0] == left:
                    currMinStk.pop(0)
                left += 1; right += 1
        maxLen = max(maxLen, right - left)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/147219960/

60 / 60 个通过测试用例
状态：通过
执行用时: 264 ms
内存消耗: 17.8 MB

执行用时：264 ms, 在所有 Python 提交中击败了97.44%的用户
内存消耗：17.8 MB, 在所有 Python 提交中击败了79.49%的用户
"""
