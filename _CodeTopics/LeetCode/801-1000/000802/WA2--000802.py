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
                    return 1
                else:
                    nonTerminuses[0].add(nodeID)
                    return 0
                currSet.remove(nodeID)
                
        for i in range(length):
            memorize_search(i, set([]))
        return list(terminuses[0])
        
"""
https://leetcode-cn.com/submissions/detail/203685545/

60 / 112 个通过测试用例
状态：解答错误

最后执行的输入：
[[1,3,4,5,7,9],[1,3,8,9],[3,4,5,8],[1,8],[5,7,8],[8,9],[7,8,9],[3],[],[]]
输出：
[8,9,5]
预期结果：
[5,8,9]
"""
