import bisect
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        length = len(nums)
        res = 0
        for i in range(length-2):
            if nums[i] == 0:
                continue
            for j in range(i+1, length-1):
                target = nums[i] + nums[j] - 1
                k = bisect.bisect_right(nums, target)
                res += k - 1 - j
        return res
        
"""
https://leetcode-cn.com/submissions/detail/202958801/

241 / 241 个通过测试用例
状态：通过
执行用时: 1608 ms
内存消耗: 13 MB

执行用时：1608 ms, 在所有 Python 提交中击败了24.28%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了72.86%的用户
"""
