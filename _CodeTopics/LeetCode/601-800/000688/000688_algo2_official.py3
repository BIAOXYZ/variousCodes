class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        def is_legal_coor(coor):
            x, y = coor
            return 0 <= x < n and 0 <= y < n
        
        # 其实开始看到 k = 100 的时候就隐约觉得可能不是回溯，但是太晚了状态也一般，还是
        # 被 n = 25 给蒙蔽了（其实就算 25 可能也会超时的，感觉回溯的话好像一般 16 就极限了）。
        # 也想到了动态规划，但是没有深入往下细想，结果果然回溯超时，就是用dp。。。

        # 参考官方答案，dp[step][i][j] 表示从 (i,j) 出发，在第 step 步时仍在棋盘上的概率。
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        for step in range(k+1):
            for x in range(n):
                for y in range(n):
                    if step == 0:
                        dp[step][x][y] = 1
                    else:
                        for dx, dy in directions:
                            if is_legal_coor((x+dx,y+dy)):
                                dp[step][x][y] += (1/8) * dp[step-1][x+dx][y+dy]
        return dp[k][row][column]
        
"""
https://leetcode-cn.com/submissions/detail/269282268/

执行用时：472 ms, 在所有 Python3 提交中击败了7.80%的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了26.95%的用户
通过测试用例：
22 / 22
"""
