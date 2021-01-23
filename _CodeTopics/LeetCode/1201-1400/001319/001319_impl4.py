class Union_Find(object):
    def __init__(self, n):
        self.fa = {i:i for i in range(n)}
        self.rank = [1] * n
        # 这里类似官方答案，给并查集对象的等价类（这里是指连通分量）引入一个总数，
        # 后面每合并一次，等价类数量减一。
        self.numOfConnectedComponent = n
    def find_with_path_compress(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find_with_path_compress(self.fa[x])
        return self.fa[x]
    def union_with_rank(self, x, y):
        fx, fy = self.find_with_path_compress(x), self.find_with_path_compress(y)
        if fx == fy:
            return
        if self.rank[fy] < self.rank[fx]:
            self.fa[fy] = fx
        elif self.rank[fy] > self.rank[fx]:
            self.fa[fx] = fy
        else:
            self.fa[fy] = fx
            self.rank[fx] += 1
        self.numOfConnectedComponent -= 1
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
        
        return uf.numOfConnectedComponent - 1
        
"""
https://leetcode-cn.com/submissions/detail/140546354/

36 / 36 个通过测试用例
状态：通过
执行用时: 156 ms
内存消耗: 27 MB

执行用时：156 ms, 在所有 Python 提交中击败了61.54%的用户
内存消耗：27 MB, 在所有 Python 提交中击败了61.54%的用户
"""
