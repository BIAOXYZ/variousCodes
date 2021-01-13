class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find(x):
            if fa[x] == x:
                return fa[x]
            else:
                return find(fa[x])
        
        def union(x, y):
            fa[find(x)] = find(y)

        n = len(edges)
        fa = {i:i for i in range(1, n+1)}
        for edge in edges:
            if find(edge[0]) != find(edge[1]):
                union(edge[0], edge[1])
            else:
                return edge
        
"""
https://leetcode-cn.com/submissions/detail/138227629/

39 / 39 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.6 MB

执行用时：36 ms, 在所有 Python 提交中击败了91.84%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了16.95%的用户
"""
