class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        length = len(graph)
        lengthInFuncion = [length]
        globalState = [float('inf') for i in range(length)]

        def backtrack(currNode, currNodeList, currNodeSet):
            if len(currNodeSet) == lengthInFuncion[0]:
                globalState[currNode] = min(len(currNodeList), globalState[currNode])
                return
            # 这里需要保证不走重复路线，但是按一般的DFS/BFS里的visited不行，因为有些路线必须有某些重复点。。。
            # 所以到这暂时不知道怎么搞了，也不打算花太多时间想了，提交一个留个记录就得了。
            if len(currNodeList) > 2 and currNode == currNodeList[-2] and currNodeList[-1] == currNodeList[-3]:
                return
            for nextNode in graph[currNode]:
                needRemove = True
                if currNode not in currNodeSet:
                    currNodeSet.add(currNode)
                else:
                    needRemove = False
                backtrack(nextNode, currNodeList + [currNode], currNodeSet)
                if needRemove:
                    currNodeSet.remove(currNode)
        
        for i in range(length):
            backtrack(i, [], set())
        return min(globalState)
        
"""
https://leetcode-cn.com/submissions/detail/204083880/

0 / 49 个通过测试用例
状态：超出时间限制

最后执行的输入：
[[1,2,3],[0],[0],[0]]
"""
