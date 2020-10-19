class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        """
        思路：比如对于输入 [[1,3], [0,2], [1,3], [0,2]] 中的第一个元素[1,3]，其实是暗含了
              0-1、0-3是边，也就是1和3肯定在一组，0在另一组。
        """

        length = len(graph)
        s1, s2 = set(), set()

        for i in range(length):
            tempset = set(graph[i])
            if i in s1 and i in s2:
                return False
            elif i in s1:
                s2 = s2.union(tempset)
            elif i in s2:
                s1 = s1.union(tempset)
            else:
                if s1.intersection(tempset) and s2.intersection(tempset):
                    return False
                elif s1.intersection(tempset):
                    s1 = s1.union(tempset)
                    s2.add(i)
                elif s2.intersection(tempset):
                    s2 = s2.union(tempset)
                    s1.add(i)
                # 其实这个可以和上面那个elif合并成一个，但是为了逻辑清晰还是分开。
                else:
                    s1.add(i)
                    s2 = s2.union(tempset)
            # 也可以用 & 来求两个集合的交集，用 | 求并集。
            if s1 & s2:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/88383865/

76 / 78 个通过测试用例
状态：解答错误

输入：[[3],[2,4],[1],[0,4],[1,3]]
输出：false
预期：true
"""
