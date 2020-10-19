class Solution(object):
    hasRing = False
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        visited = [False for i in range(numCourses)]
        # 后来发现不注释这个定义，然后下面dfs函数里用global hasRing还是不行，只好先用类成员变量了。
        # hasRing = False

        # 构造邻接表
        # edges = {}
        # for elem in prerequisites:
        #     if not edges.has_key(elem[1]):
        #         edges[elem[1]] = [elem[0]]
        #     else:
        #         edges[elem[1]].append(elem[0])
        # print edges

        edges = collections.defaultdict(list)
        for info in prerequisites:
            edges[info[1]].append(info[0])
        ##print edges

        def dfs(vertex):
            # python2没有nonlocal关键词，只好用global了。当然也可以把这个变量定义成类的
            # 一个成员，但是那样更丑了其实。
            # global hasRing
            visited[vertex] = "ongoing"
            for v in edges[vertex]:
                if visited[v] == False:
                    dfs(v)
                    if self.hasRing:
                        return
                elif visited[v] == "ongoing":
                    self.hasRing = True
                    return
            visited[vertex] = True

        for i in range(numCourses):
            if not self.hasRing and not visited[i]:
                dfs(i)
        return not self.hasRing
        
"""
https://leetcode-cn.com/submissions/detail/94672410/

46 / 46 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：15.8 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了65.23%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了5.55%的用户
"""
