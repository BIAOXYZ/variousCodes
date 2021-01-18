class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find_with_set(x):
            if not fa.has_key(x):
                fa[x] = set([x])
            return fa[x]
        
        def union_with_set(x, y):
            fx, fy = find_with_set(x), find_with_set(y)
            # 笨办法（`000684.py`）改进版：干脆直接算个结果出来，一个个赋值就完了。
            # 底层实现上应该每一种都是一层循环，比前面那个两层循环应该是要快。
            tmp = fx | fy
            for elem in list(fx) + list(fy):
                fa[elem] = tmp

        n = len(edges)
        """
        # 也可以直接初始化好，这样find相关的函数里就不用考虑key不存在的情形了。
        # fa = {i:set([i]) for i in range(1, n+1)}
        """
        fa = {}
        for edge in edges:
            ##print "1:", fa
            if find_with_set(edge[0]) != find_with_set(edge[1]):
                ##print "2:", fa
                union_with_set(edge[0], edge[1])
            else:
                return edge
            ##print "after union:", fa
        
"""
https://leetcode-cn.com/submissions/detail/139442930/

39 / 39 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 13.8 MB

执行用时：60 ms, 在所有 Python 提交中击败了17.56%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了9.14%的用户
"""
