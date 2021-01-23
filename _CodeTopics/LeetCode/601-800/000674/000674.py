class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        maxLen = 1
        currLen = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currLen += 1
            else:
                maxLen = max(maxLen, currLen)
                currLen = 1
        
        # 循环出来后还得再来一次这个操作，不然最后一个currLen如果是最大的就漏掉了。
        maxLen = max(maxLen, currLen)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/140655246/

36 / 36 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.9 MB

执行用时：24 ms, 在所有 Python 提交中击败了67.63%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了50.00%的用户
"""
