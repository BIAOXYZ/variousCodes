class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def find_and_compress(x):
            if x != fa[x]:
                fa[x] = find_and_compress(fa[x])
            return fa[x]

        def union_big_as_father(x, y):
            fa[x] = find_and_compress(x)
            fa[y] = find_and_compress(y)
            if fa[x] == fa[y]:
                return
            else:
                if fa[x] > fa[y]:
                    fa[fa[y]] = fa[x]
                else:
                    fa[fa[x]] = fa[y]
        
        n = len(isConnected)
        fa = {i:i for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union_big_as_father(i, j)
        
        res = 0
        for i in range(n):
            if fa[i] == i:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/137206904/

113 / 113 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.3 MB

执行用时：40 ms, 在所有 Python 提交中击败了55.35%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了55.52%的用户
"""
