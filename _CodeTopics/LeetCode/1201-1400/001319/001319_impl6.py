class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        # 非class版本的，带按秩合并的写法。承接上一个（`001319_impl5.py`），
        # 额外添加了一个变量（因为子函数里要用，所以还是比较别扭的那种用list的办法）来记录全局的等价类（这里是指连通分量）数目。

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
            numOfConnectedComponent[0] -= 1

        length = len(connections)
        if length < n - 1:
            return -1
        
        fa = {i:i for i in range(n)}
        rank = [1] * n
        numOfConnectedComponent = [n]
        for edge in connections:
            union_with_rank(edge[0], edge[1])
        
        return numOfConnectedComponent[0] - 1
        
"""
https://leetcode-cn.com/submissions/detail/140553834/

36 / 36 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 27.2 MB

执行用时：124 ms, 在所有 Python 提交中击败了88.46%的用户
内存消耗：27.2 MB, 在所有 Python 提交中击败了53.85%的用户
"""
