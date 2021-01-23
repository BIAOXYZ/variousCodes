class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        # 非class版本的，带按秩合并的写法。主要是为了修正 `001319_impl--(with-flaw).py` 。

        def find_with_path_compress(x):
            if fa[x] != x:
                fa[x] = find_with_path_compress(fa[x])
            return fa[x]
        def union_with_rank(x, y):
            fx, fy = find_with_path_compress(x), find_with_path_compress(y)
            if fx == fy:
                return
            if rank[fy] < rank[fx]:
                fa[fy] = fx
            elif rank[fy] > rank[fx]:
                fa[fx] = fy
            else:
                fa[fy] = fx
                rank[fx] += 1

        length = len(connections)
        if length < n - 1:
            return -1
        
        fa = {i:i for i in range(n)}
        rank = [1] * n
        for edge in connections:
            union_with_rank(edge[0], edge[1])
        
        fa = {i:find_with_path_compress(i) for i in range(n)}
        return len(set(fa.values())) - 1
        
"""
https://leetcode-cn.com/submissions/detail/140551333/

36 / 36 个通过测试用例
状态：通过
执行用时: 148 ms
内存消耗: 29.7 MB

执行用时：148 ms, 在所有 Python 提交中击败了76.92%的用户
内存消耗：29.7 MB, 在所有 Python 提交中击败了46.15%的用户
"""
