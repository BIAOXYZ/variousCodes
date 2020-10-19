class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def calculate_distance(i,j):
            start, end = min(i,j), max(i,j)
            if dp[start][end] != 0:
                return dp[start][end]
            currPath = [start]
            for ind in range(end) + range(end+1,N):
                currPath.append(ind)
                if dp[start][ind] == 0:
                    currPath.pop()
                    continue
                else:
                    backtrack_dfs(currPath, end)
                    currPath.pop()
                    if dp[start][end] != 0:
                        return dp[start][end]

        def backtrack_dfs(currPath, end):
            if dp[currPath[-1]][end] != 0:
                dp[currPath[0]][end] = dp[currPath[-1]][end] + len(currPath) - 1
                dp[end][currPath[0]] = dp[currPath[-1]][end] + len(currPath) - 1
            elif dp[currPath[-1]][end] == 0:
                for ind in range(end) + range(end+1,N):
                    if ind not in currPath and dp[currPath[-1]][ind] != 0:
                        currPath.append(ind)
                        backtrack_dfs(currPath, end)
                        currPath.pop()

        def init_dp(edges):
            for edge in edges:
                dp[edge[0]][edge[1]] = 1
                dp[edge[1]][edge[0]] = 1

        dp = [[0 for i in range(N)] for j in range(N)]
        init_dp(edges)
        print dp

        res = []
        for i in range(N):
            sum = 0
            for j in range(i) + range(i+1,N):
                distIJ = calculate_distance(j,i) if j < i else calculate_distance(i,j)
                sum += distIJ
            res.append(sum)
            print dp
        return res
        
"""
https://leetcode-cn.com/submissions/detail/113719283/

10 / 69 个通过测试用例
状态：解答错误

输入：
6
[[0,1],[0,2],[2,3],[2,4],[2,5]]
输出：
[8,12,6,12,12,12]
预期：
[8,12,6,10,10,10]
"""
