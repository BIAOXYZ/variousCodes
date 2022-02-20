class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # 2022.02.21 重写一遍官方版本（变量名不全一样），既为了再次熟悉，也为了将来更好总结复习。
        # 不过官方版本的父亲表示是数组，我过去多用字典。
        # PS：后来发现以后复习并查集的话只要看 https://oi-wiki.org/ds/dsu/ 就够了。

        # 这个是带了路径压缩的写法
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        
        def union(x, y):
            fa[find(x)] = find(y)

        n = len(isConnected)
        fa = list(range(n))
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        circles = sum(fa[i] == i for i in range(n))
        return circles
        
"""
https://leetcode-cn.com/submissions/detail/270976202/

执行用时：52 ms, 在所有 Python3 提交中击败了50.57%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了44.66%的用户
通过测试用例：
113 / 113
"""
