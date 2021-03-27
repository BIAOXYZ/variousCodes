class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 手动狗头题
        return sorted(arr)[:k]
        
"""
https://leetcode-cn.com/submissions/detail/160659509/

38 / 38 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 14.1 MB

执行用时：48 ms, 在所有 Python 提交中击败了79.29%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了79.02%的用户
"""
