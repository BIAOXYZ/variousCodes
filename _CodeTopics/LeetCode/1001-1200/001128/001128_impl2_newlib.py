from collections import defaultdict 
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        ddic = defaultdict(int)
        for x, y in dominoes:
            x, y = min(x,y), max(x,y)
            currKey = tuple([x,y])
            ddic[currKey] += 1

        res = 0
        for v in ddic.values():
            if v >= 2:
                res += v * (v-1) / 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/141165962/

19 / 19 个通过测试用例
状态：通过
执行用时: 208 ms
内存消耗: 24.8 MB

执行用时：208 ms, 在所有 Python 提交中击败了76.06%的用户
内存消耗：24.8 MB, 在所有 Python 提交中击败了18.31%的用户
"""
