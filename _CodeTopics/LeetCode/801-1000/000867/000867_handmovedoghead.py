class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        # 手动狗头题
        return zip(*matrix)
        
"""
https://leetcode-cn.com/submissions/detail/148455206/

36 / 36 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.8 MB

执行用时：24 ms, 在所有 Python 提交中击败了97.70%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了70.25%的用户
"""
