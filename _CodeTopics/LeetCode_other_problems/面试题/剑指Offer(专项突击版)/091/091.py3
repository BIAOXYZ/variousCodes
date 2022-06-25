class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        m, n = len(costs), 3
        dp = [[-1 for _ in range(3)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if x == 0:
                    dp[x][y] = costs[x][y]
                else:
                    dp[x][y] = min(dp[x-1][(y-1)%3], dp[x-1][(y+1)%3]) + costs[x][y]
        return min(dp[m-1])
        
"""
https://leetcode.cn/submissions/detail/329269184/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
24.23%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
33.20%
的用户
通过测试用例：
100 / 100
"""
