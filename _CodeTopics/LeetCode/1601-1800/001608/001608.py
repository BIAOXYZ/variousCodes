import bisect
class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = len(nums)
        for i in range(1, n+1):
            ind = bisect.bisect_left(nums, i)
            if n - ind == i:
                return i
        return -1
        
"""
https://leetcode.cn/submissions/detail/361830447/

执行用时：
16 ms
, 在所有 Python 提交中击败了
84.88%
的用户
内存消耗：
12.9 MB
, 在所有 Python 提交中击败了
73.26%
的用户
通过测试用例：
98 / 98
"""
