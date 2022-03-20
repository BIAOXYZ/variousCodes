class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        # 官方题解，主要又忙，又急着上厕所，前面一个还WA了。
        # 此外，打算一会单步看下官方 BFS 会不会有栈节点重复添加（但不影响正确性）的问题。

        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n
        vis[0] = True
        q = deque([0])
        ans, dist = 0, 1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if vis[v]:
                        continue
                    vis[v] = True
                    q.append(v)
                    ans = max(ans, (dist * 2 - 1) // patience[v] * patience[v] + dist * 2 + 1)
            dist += 1
        return ans
        
"""
https://leetcode-cn.com/submissions/detail/286378092/

执行用时：600 ms, 在所有 Python3 提交中击败了59.09%的用户
内存消耗：45.8 MB, 在所有 Python3 提交中击败了100.00%的用户
通过测试用例：
50 / 50
"""
