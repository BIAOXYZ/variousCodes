class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        visited = [False for i in range(numCourses)]
        hasRing = False

        # 构造邻接表
        edges = {}
        for elem in prerequisites:
            if not edges.has_key(elem[1]):
                edges[elem[1]] = [elem[0]]
            else:
                edges[elem[1]].append(elem[0])
        print edges

        def dfs(vertex):
            # python2没有nonlocal关键词，只好用global了。当然也可以把这个变量定义成类的
            # 一个成员，但是那样更丑了其实。
            global hasRing
            visited[vertex] = "ongoing"
            for v in edges[vertex]:
                if visited[v] == False:
                    dfs(v)
                    if hasRing:
                        return
                elif visited[v] == "ongoing":
                    hasRing = True
                    return
            visited[vertex] = True

        for i in range(numCourses):
            if not hasRing and not visited[i]:
                dfs(i)
        return hasRing
        
"""
https://leetcode-cn.com/submissions/detail/94665826/

0 / 46 个通过测试用例
状态：执行出错

执行出错信息：Line 26: KeyError: 1
最后执行的输入：2
               [[1,0]]
"""
