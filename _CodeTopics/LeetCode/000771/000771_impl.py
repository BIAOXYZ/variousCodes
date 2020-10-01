class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        return sum(ch in J for ch in S)
        
"""
https://leetcode-cn.com/submissions/detail/112802905/

254 / 254 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.4 MB

执行用时：20 ms, 在所有 Python 提交中击败了68.06%的用户
内存消耗：12.4 MB, 在所有 Python 提交中击败了59.17%的用户
"""
