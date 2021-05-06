class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """

        res = [first]
        for elem in encoded:
            res.append(elem^res[-1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/174886292/

76 / 76 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 14.5 MB

执行用时：44 ms, 在所有 Python 提交中击败了68.90%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了60.77%的用户
"""
