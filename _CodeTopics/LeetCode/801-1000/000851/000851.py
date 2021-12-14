from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """

        # dfs + （类似）记忆化

        richerDic = defaultdict(list)
        for theRich, thePoor in richer:
            richerDic[thePoor].append(theRich)

        dic = {}
        def dfs(vertex):
            if dic.has_key(vertex):
                return dic[vertex]
            se = set()
            for v in richerDic[vertex]:
                se.add(v)
                se |= dfs(v)
            dic[vertex] = se
            return dic[vertex]
        n = len(quiet)
        for i in range(n):
            dfs(i)
        
        # 这个鸟函数应该能用更简洁的写法替代，但是太晚了，赶紧提交一个睡了。
        def get_key_for_min_val(i):
            minQuiteKey, minQuiteVal = i, quiet[i]
            richerSet = dic[i]
            for j in richerSet:
                if quiet[j] < minQuiteVal:
                    minQuiteKey, minQuiteVal = j, quiet[j]
            return minQuiteKey
        return [get_key_for_min_val(i) for i in range(n)]
        
"""
https://leetcode-cn.com/submissions/detail/248587450/

执行用时：208 ms, 在所有 Python 提交中击败了11.11%的用户
内存消耗：27.4 MB, 在所有 Python 提交中击败了11.11%的用户
通过测试用例：
86 / 86
"""
