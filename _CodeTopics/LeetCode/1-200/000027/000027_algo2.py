class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # 倒序循环删除法
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
        
"""
https://leetcode-cn.com/submissions/detail/124582850/

113 / 113 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB

Accepted
113/113 cases passed (20 ms)
Your runtime beats 67.32 % of python submissions
Your memory usage beats 18.86 % of python submissions (12.9 MB)
"""
"""
第一次用VS Code的LeetCode插件在本地做题+测试+提交。
"""
