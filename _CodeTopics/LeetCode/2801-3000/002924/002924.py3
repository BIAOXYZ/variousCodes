class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        possibleChampions = set(range(n))
        for stronger, weaker in edges:
            if weaker in possibleChampions:
                possibleChampions.remove(weaker)
        if len(possibleChampions) != 1:
            return -1
        return list(possibleChampions)[0]
        
"""
https://leetcode.cn/problems/find-champion-ii/submissions/523240590?envType=daily-question&envId=2024-04-13

通过
零知识证明
提交于 2024.04.13 22:24

执行用时分布
63
ms
击败
77.98%
使用 Python3 的用户
消耗内存分布
17.34
MB
击败
91.74%
使用 Python3 的用户
"""
