class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        res = 0
        for ch in S:
            if ch in J:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/112802790/

254 / 254 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.3 MB

执行用时：28 ms, 在所有 Python 提交中击败了17.55%的用户
内存消耗：12.3 MB, 在所有 Python 提交中击败了83.62%的用户
"""
