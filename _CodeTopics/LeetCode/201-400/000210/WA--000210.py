class Solution(object):
    
    hasRing = False

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # 和 `LC207. 课程表` 官方答案很像，下面这个提交也是改了下官方答案，更易懂。
        # https://leetcode-cn.com/submissions/detail/94672410/

        visited = [False for i in range(numCourses)]
        res = []
        
        edges = collections.defaultdict(list)
        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(vertex):
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
            # LC207 的话就没必要搞这个栈了，因为只需要判断拓扑排序是否存在。
            # 而这道题要求如果存在的话要输出一个拓扑排序。
            res.append(vertex)

        for i in range(numCourses):
            if not self.hasRing and not visited[i]:
                dfs(i)
        return res[::-1]
        
"""
https://leetcode-cn.com/submissions/detail/248245230/

39 / 44 个通过测试用例
状态：解答错误

输入：
3
[[1,0],[2,0],[0,2]]
输出：
[1]
预期结果：
[]
"""
