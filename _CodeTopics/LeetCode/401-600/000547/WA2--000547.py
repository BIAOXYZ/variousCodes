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
        
        # 如果没有这样第二次再来一遍的话，对于输入 [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]] 就会输出错误答案2，
        # 实际上正确答案应该是1。因为这个矩阵第一次循环，fa的变化情况如下：
        # {1:1, 2:2, 3:3, 4:4} --> {1:1, 2:2, 3:3, 4:1} --> {1:1, 2:2, 3:2, 4:1} --> {1:1, 2:2, 3:1, 4:1} --> 不变
        # 但是其实2的father也应该是1，只是2只能通过3更新，但是3的father从2变成1后，后面没法再改2的father了。
        # 因此，把整个循环在一模一样重新搞一遍应该就可以了。
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len(set(fa.values()))
        
"""
https://leetcode-cn.com/submissions/detail/137051061/

输入：
[[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
输出：
4
预期：
3
"""
