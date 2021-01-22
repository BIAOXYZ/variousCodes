class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        def find(x):
            if fa[x] == x:
                return x
            else:
                return find(fa[x])
        def union(x, y):
            fx, fy = find(x), find(y)
            if fx < fy:
                fa[fy] = fx
            else:
                fa[fx] = fy

        # 如果边的数量小于n-1，一定不可能成连通图；反之，一定可以。
        length = len(connections)
        if length < n - 1:
            return -1
        
        # 每拆一条边，可以消除一个连通分量，直到最后只剩一个连通分量（也就是全部联通）。
        # 所以其实结果就是 `总的联通分量数-1`。
        
        fa = {i:i for i in range(n)}
        for edge in connections:
            union(edge[0], edge[1])
        
        fa = {i:find(i) for i in range(n)}
        return len(set(fa.values())) - 1
        
"""
https://leetcode-cn.com/submissions/detail/140447902/

36 / 36 个通过测试用例
状态：通过
执行用时: 140 ms
内存消耗: 29.1 MB

执行用时：140 ms, 在所有 Python 提交中击败了80.77%的用户
内存消耗：29.1 MB, 在所有 Python 提交中击败了46.15%的用户
"""
