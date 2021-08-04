class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        # 用了记忆化搜索的方法，应该是可以的吧。。。

        length = len(graph)
        # set 类型也不行，必须得用这种比较chuo的外面包一层list的形式！
        terminuses = [set()]
        nonTerminuses = [set()]
        for i in range(length):
            if graph[i] == []:
                terminuses[0].add(i)
        
        def memorize_search(nodeID, currSet):
            if nodeID in nonTerminuses[0] or nodeID in terminuses[0]:
                return
            if nodeID in currSet:
                for elem in currSet:
                    nonTerminuses[0].add(elem)
                return
            else:
                if all([nextNodeID in terminuses[0] for nextNodeID in graph[nodeID]]):
                    terminuses[0].add(nodeID)
                    return
                for nextNodeID in graph[nodeID]:
                    if nextNodeID in nonTerminuses[0]:
                        nonTerminuses[0].add(nodeID)
                        return
                    else:
                        currSet.add(nodeID)
                        memorize_search(nextNodeID, currSet)
                        currSet.remove(nodeID)
        
        for i in range(length):
            memorize_search(i, set([]))
        return list(terminuses[0])
        
"""
https://leetcode-cn.com/submissions/detail/203392108/

49 / 112 个通过测试用例
状态：解答错误

最后执行的输入：
[[],[0,2,3,4],[3],[4],[]]
输出：
[0,2,3,4]
预期结果：
[0,1,2,3,4]
"""
