class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 手动狗头题2。
        return set(range(len(nums) + 1)).difference(set(nums)).pop()
        
"""
https://leetcode-cn.com/submissions/detail/236017135/

执行用时：20 ms, 在所有 Python 提交中击败了91.75%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了7.91%的用户
通过测试用例：
122 / 122
"""
