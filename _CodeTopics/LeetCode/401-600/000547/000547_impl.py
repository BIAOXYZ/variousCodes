class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        # 用无路径压缩的普通find也是可以的，所以前面三个错的问题主要是出在union的时候：
        # 当要用y的father取代x的father时，应该是 fa[fa[x]] = fa[y] 而不是 fa[x] = fa[y] !!!!!
        # 所以 LC785 的那个实现 `000785_algo3.py` 其实不标准，以后不要参考了。
        # 真正的标准的实现是更早的 LC990 的 `000990_algo2_2.py`。
        def find(x):
            if x == fa[x]:
                return x
            else:
                return find(fa[x])

        def union_big_as_father(x, y):
            fa[x] = find(x)
            fa[y] = find(y)
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
https://leetcode-cn.com/submissions/detail/137209969/

113 / 113 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.6 MB

执行用时：36 ms, 在所有 Python 提交中击败了70.15%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了34.79%的用户
"""
