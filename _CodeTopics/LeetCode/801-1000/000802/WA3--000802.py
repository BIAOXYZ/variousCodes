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
        return sorted(list(terminuses[0]))
        
"""
https://leetcode-cn.com/submissions/detail/203687112/

79 / 112 个通过测试用例
状态：解答错误

最后执行的输入：
[[2,3,4,7,9],[12,13,15,19],[9],[3,13],[2,9,14,15,19],[6,15,18],[13],[13,14,17,18,19],[10,15],[16],[15],[13,15,16,17,19],[5,14,15,16,17],[9,18,19],[13,15,16,17,18,19],[1,16,17,18,19],[17,19],[18,19],[],[]]
输出：
[2,9,16,17,18,19]
预期结果：
[2,6,9,13,16,17,18,19]
"""
