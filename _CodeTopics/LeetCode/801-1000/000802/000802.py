class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        length = len(graph)
        # set 类型也不行，必须得用这种比较chuo的外面包一层list的形式！
        terminuses = [set()]
        nonTerminuses = [set()]
        for i in range(length):
            if graph[i] == []:
                terminuses[0].add(i)
        
        def memorize_search(nodeID, currSet):
            if nodeID in nonTerminuses[0]:
                for elem in currSet:
                    nonTerminuses[0].add(elem)
                return 0
            if nodeID in terminuses[0]:
                return 1
            if nodeID in currSet:
                for elem in currSet:
                    nonTerminuses[0].add(elem)
                return 0
            else:
                currSet.add(nodeID)
                if all([memorize_search(nextNodeID, currSet) for nextNodeID in graph[nodeID]]):
                    terminuses[0].add(nodeID)
                    currSet.remove(nodeID)
                    return 1
                else:
                    nonTerminuses[0].add(nodeID)
                    currSet.remove(nodeID)
                    return 0
        
        for i in range(length):
            memorize_search(i, set([]))
        return sorted(list(terminuses[0]))
        
"""
https://leetcode-cn.com/submissions/detail/203695249/

112 / 112 个通过测试用例
状态：通过
执行用时: 228 ms
内存消耗: 18.9 MB

执行用时：228 ms, 在所有 Python 提交中击败了30.00%的用户
内存消耗：18.9 MB, 在所有 Python 提交中击败了56.67%的用户
"""
