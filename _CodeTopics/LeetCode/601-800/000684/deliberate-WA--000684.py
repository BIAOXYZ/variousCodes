class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find(x):
            if not fa.has_key(x):
                fa[x] = set([x])
            return fa[x]
        
        def union_with_set(x, y):
            fx, fy = find(x), find(y)
            """
            # 这里用下面这句会有问题，无法同步更新所有数字对应的set
            # fa[x] = fa[y] = fx | fy
            """
            flag = True if fx == fy else False
            """
            # 换成这两句也不行，还是不会更新前面的那个集合。后来查了下才知道，得用update()，此外还有intersection_update()等接口。
            # fa[x].union(fy)
            # fa[y].union(fx)
            """
            """
            # mmp，换完还不行。草泥马。直接提交了。。。
            """
            fa[x].update(fy)
            fa[y].update(fx)
            return flag

        fa = {}
        for edge in edges:
            if union_with_set(edge[0], edge[1]):
                return edge
            print fa
        
"""
https://leetcode-cn.com/submissions/detail/138226034/

0 / 39 个通过测试用例
状态：解答错误

输入：
[[1,2],[1,3],[2,3]]
输出：
[]
预期：
[2,3]
"""
