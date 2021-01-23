class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        def find_with_path_compress(x):
            if fa[x] != x:
                fa[x] = find_with_path_compress(fa[x])
            return fa[x]
        def union_with_rank(x, y):
            fx, fy = find_with_path_compress(x), find_with_path_compress(y)
            if rank[fy] < rank[fx]:
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
        # 第一次使用按秩合并的union，需要引入额外的存储空间。这里用了一个rank数组。
        # 其实也可以把fa的元素的值搞成 [father, rank]就行。
        rank = [1] * n
        for edge in connections:
            union_with_rank(edge[0], edge[1])
        
        fa = {i:find_with_path_compress(i) for i in range(n)}
        return len(set(fa.values())) - 1
        
"""
https://leetcode-cn.com/submissions/detail/140515736/

36 / 36 个通过测试用例
状态：通过
执行用时: 156 ms
内存消耗: 29.6 MB

执行用时：156 ms, 在所有 Python 提交中击败了61.54%的用户
内存消耗：29.6 MB, 在所有 Python 提交中击败了46.15%的用户
"""
