class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        def find(x):
            if x == fa[x]:
                return x
            else:
                # 如果不带路径压缩的话就一句 `return find(fa[x])` 代替下面两句即可。
                fa[x] = find(fa[x])
                return fa[x]
        
        def union(x,y):
            fa[x], fa[y] = find(x), find(y)
            if fa[x] == fa[y]:
                return
            else:
                if fa[x] > fa[y]: fa[x] = fa[y]
                else: fa[y] = fa[x]

        def unionall(l):
            if not l:
                return
            n = len(l)
            for i in range(1,n):
                union(l[0],l[i])

        if not graph:
            return True
        length = len(graph)
        fa = [i for i in range(length)]

        for i in range(length):
            if graph[i] == []:
                continue
            unionall(graph[i])
            if find(i) == find(graph[i][0]):
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/88501689/

78 / 78 个通过测试用例
状态：通过
执行用时：180 ms
内存消耗：13 MB
"""
"""
执行用时：180 ms, 在所有 Python 提交中击败了49.06%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了50.00%的用户
"""
