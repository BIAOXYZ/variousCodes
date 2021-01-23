class Solution(object):
    # 这里随便初始化什么值都行，因为后面反正还要赋值成n。
    numOfConnectedComponent = 0
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        # 非class版本的，带按秩合并的写法。承接上一个（`001319_impl6.py`），
        # 额外添加了一个变量（这次用类成员变量的办法，而不是比较别扭的list的第一个元素的办法）来记录等价类数目。

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
            self.numOfConnectedComponent -= 1

        length = len(connections)
        if length < n - 1:
            return -1
        
        fa = {i:i for i in range(n)}
        rank = [1] * n
        self.numOfConnectedComponent = n

        for edge in connections:
            union_with_rank(edge[0], edge[1])
        
        return self.numOfConnectedComponent - 1
        
"""
https://leetcode-cn.com/submissions/detail/140557325/

36 / 36 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 27 MB

执行用时：132 ms, 在所有 Python 提交中击败了84.62%的用户
内存消耗：27 MB, 在所有 Python 提交中击败了61.54%的用户
"""
