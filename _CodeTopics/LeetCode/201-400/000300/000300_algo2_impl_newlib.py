import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 同样是官方答案贪心 + 二分查找方法的思路，只不过这次用库实现二分查找部分。

        length = len(nums)
        d = [nums[0]]

        for i in range(1, length):
            if nums[i] > d[-1]:
                d.append(nums[i])
            else:
                loc = bisect.bisect_left(d, nums[i])
                d[loc] = nums[i]
        return len(d)
        
"""
https://leetcode-cn.com/submissions/detail/151173818/

54 / 54 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.3 MB

执行用时：36 ms, 在所有 Python 提交中击败了93.89%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了55.10%的用户
"""
