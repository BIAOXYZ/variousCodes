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
            # ！！！！！!!!!!
            # 因为没想到怎么公用一个set做多个点的father，所以只能用这种笨办法：
            # 在union的时候，x的father（是个集合）里的每个元素的father都把y的father里的每个元素加进去；对于y来说也是一样的。
            # （只不过这里不想再写一轮for循环，因此直接用了类似并集的操作update，但是其实质还是两层循环）
            # TODO： 1.我怀疑用C++处理这种情况反而好写些。2.另外还是得继续探索下Python到底怎么搞这种情况。
            for elem in list(fx):
                fa[elem].update(fy)
            for elem in list(fy):
                fa[elem].update(fx)

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
https://leetcode-cn.com/submissions/detail/139130718/

39 / 39 个通过测试用例
状态：通过
执行用时: 280 ms
内存消耗: 77.7 MB

执行用时：280 ms, 在所有 Python 提交中击败了5.34%的用户
内存消耗：77.7 MB, 在所有 Python 提交中击败了5.09%的用户
"""
