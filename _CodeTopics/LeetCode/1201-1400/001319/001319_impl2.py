# 第一次把并查集独立成一个class来写。
class Union_Find(object):
    def __init__(self, n):
        self.fa = {i:i for i in range(n)}
        self.rank = [1] * n
    def find_with_path_compress(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find_with_path_compress(self.fa[x])
        return self.fa[x]
    def union_with_rank(self, x, y):
        fx, fy = self.find_with_path_compress(x), self.find_with_path_compress(y)
        if self.rank[fy] < self.rank[fx]:
            self.fa[fy] = fx
        else:
            self.fa[fx] = fy
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        length = len(connections)
        if length < n - 1:
            return -1
        
        uf = Union_Find(n)
        for edge in connections:
            uf.union_with_rank(edge[0], edge[1])
        
        uf.fa = {i:uf.find_with_path_compress(i) for i in range(n)}
        return len(set(uf.fa.values())) - 1
        
"""
https://leetcode-cn.com/submissions/detail/140518573/

36 / 36 个通过测试用例
状态：通过
执行用时: 200 ms
内存消耗: 29.4 MB

执行用时：200 ms, 在所有 Python 提交中击败了53.85%的用户
内存消耗：29.4 MB, 在所有 Python 提交中击败了46.15%的用户
"""
