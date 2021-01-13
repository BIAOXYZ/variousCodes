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
            # 上一个错的实现是总想着把每个元素对应的set的值都统一同步，然后到最后形成圈的那条边出现时，
            # edge的两个节点所对应的两个set应该是相等的。但是怎么都做不到同步。。。
            # 所以这次换个思路：当形成圈的那条边出现时，一定至少有 x in fy 或 y in fx 两条件之一满足。
            if x in fy or y in fx:
                flag = True
            else:
                flag = False
            fa[x] = fa[y] = fx | fy
            return flag

        fa = {}
        for edge in edges:
            if union_with_set(edge[0], edge[1]):
                return edge
        
"""
https://leetcode-cn.com/submissions/detail/138226824/

18 / 39 个通过测试用例
状态：解答错误

输入：
[[3,4],[1,2],[2,4],[3,5],[2,5]]
输出：
[]
预期：
[2,5]
"""
