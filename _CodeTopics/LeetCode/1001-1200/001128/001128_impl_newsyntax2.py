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
            """
            dic.setdefault(currKey, 0)
            dic[currKey] += 1
            """
            # 上面两句等价于下边一句：
            dic[currKey] = dic.setdefault(currKey, 0) + 1

        res = 0
        for v in dic.values():
            if v >= 2:
                res += v * (v-1) / 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/141165416/

19 / 19 个通过测试用例
状态：通过
执行用时: 212 ms
内存消耗: 24.9 MB

执行用时：212 ms, 在所有 Python 提交中击败了69.01%的用户
内存消耗：24.9 MB, 在所有 Python 提交中击败了5.63%的用户
"""
