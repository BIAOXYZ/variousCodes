from sortedcontainers import SortedList
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        # 用 sortedcontainers 库的话即使在leetcode平台也必须显示import。此外，用这个数据结构
        # 做这道题就是“不讲武德”吧，毕竟单调栈/队列是这个题最精髓的部分，比滑动窗口部分更精髓。
        
        length = len(nums)
        left = right = 0
        maxLen = 1
        currSortedList = SortedList([])

        while right < length:
            currSortedList.add(nums[right])
            if abs(currSortedList[-1] - currSortedList[0]) <= limit:
                right += 1
            else:
                maxLen = max(maxLen, right - left)
                currSortedList.remove(nums[left])
                left += 1
                right += 1
        maxLen = max(maxLen, right - left)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/147223107/

60 / 60 个通过测试用例
状态：通过
执行用时: 884 ms
内存消耗: 18.2 MB

执行用时：884 ms, 在所有 Python 提交中击败了53.85%的用户
内存消耗：18.2 MB, 在所有 Python 提交中击败了66.67%的用户
"""
