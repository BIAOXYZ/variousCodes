class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        arr.sort()
        return arr[:k]
        
"""
https://leetcode-cn.com/submissions/detail/214485872/

29 / 29 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 18.7 MB

执行用时：24 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：18.7 MB, 在所有 Python 提交中击败了70.90%的用户
"""
