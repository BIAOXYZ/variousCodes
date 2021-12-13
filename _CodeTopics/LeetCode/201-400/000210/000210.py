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
        return res[::-1] if not self.hasRing else []
        
"""
https://leetcode-cn.com/submissions/detail/248245338/

执行用时：20 ms, 在所有 Python 提交中击败了94.76%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了10.49%的用户
通过测试用例：
44 / 44
"""
