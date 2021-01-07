class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def find(x):
            if x == fa[x]:
                return x
            else:
                return find(fa[x])

        def union(x, y):
            fa[x] = find(x)
            fa[y] = find(y)
            if fa[x] == fa[y]:
                return
            else:
                if fa[x] < fa[y]:
                    fa[y] = fa[x]
                else:
                    fa[x] = fa[y]
        
        n = len(isConnected)
        fa = {i:i for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len(set(fa.values()))
        
"""
https://leetcode-cn.com/submissions/detail/136799511/

89 / 113 个通过测试用例
状态：解答错误

输入：
[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
输出：
2
预期：
1
"""
