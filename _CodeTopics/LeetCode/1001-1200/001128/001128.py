class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        dic = {}
        for x, y in dominoes:
            x, y = min(x,y), max(x,y)
            currKey = tuple([x,y])
            if not dic.has_key(currKey):
                dic[currKey] = 1
            else:
                dic[currKey] += 1
        
        res = 0
        for v in dic.values():
            if v >= 2:
                res += v * (v-1) / 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/141164046/

19 / 19 个通过测试用例
状态：通过
执行用时: 224 ms
内存消耗: 24.6 MB

执行用时：224 ms, 在所有 Python 提交中击败了46.48%的用户
内存消耗：24.6 MB, 在所有 Python 提交中击败了84.51%的用户
"""
