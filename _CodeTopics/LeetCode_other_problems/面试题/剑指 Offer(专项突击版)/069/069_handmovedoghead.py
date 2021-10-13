class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # 手动狗头题
        return arr.index(max(arr))
        
"""
https://leetcode-cn.com/submissions/detail/228675519/

34 / 34 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了87.50%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了41.67%的用户
"""
