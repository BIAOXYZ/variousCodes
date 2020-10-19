class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        if not graph:
            return True
        length = len(graph)
        s1, s2 = set([0]), set(graph[0])
        leftIndexes = []

        for i in range(1,length):
            # 如果graph[i]是个空集说明是孤立点，直接跳过。否则如输入 [[4],[],[4],[4],[0,2,3]]
            # 会造成下面的while死循环。
            if not graph[i]:
                continue
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
                else:
                    leftIndexes.append(i)
            if s1 & s2:
                return False
        while leftIndexes:
            i = leftIndexes.pop(0)
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
                else:
                    leftIndexes.append(i)
            if s1 & s2:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/88419160/

11 / 78 个通过测试用例
状态：超出时间限制

最后执行的输入：[[1],[0],[4],[4],[2,3]]
"""
