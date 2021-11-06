class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 手动狗头题。
        return list(set(range(len(nums) + 1)).difference(set(nums)))[0]
        
"""
https://leetcode-cn.com/submissions/detail/236016362/

执行用时：24 ms, 在所有 Python 提交中击败了76.98%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了10.65%的用户
通过测试用例：
122 / 122
"""
