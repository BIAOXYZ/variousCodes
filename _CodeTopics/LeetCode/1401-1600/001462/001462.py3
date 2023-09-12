class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        visited = [False for _ in range(numCourses)]
        edges = collections.defaultdict(list)
        for info in prerequisites:
            edges[info[0]].append(info[1])
        
        dependencies = collections.defaultdict(set)
        def dfs(vertex):
            if visited[vertex]:
                return dependencies[vertex]
            for v in edges[vertex]:
                tmp = dfs(v)
                # 对于每一个依赖 vertex 节点的 v，vertex 会把 v 和所有依赖 v 的节点
                ## 都加入到自己的依赖节点集合中。
                dependencies[vertex].add(v)
                dependencies[vertex].update(tmp)
            visited[vertex] = True
            return dependencies[vertex]

        for i in range(numCourses):
            if not visited[i]:
                dfs(i)
        res = [-1] * len(queries) 
        for i, course in enumerate(queries):
            course0, course1 = course
            if course1 in dependencies[course0]:
                res[i] = True
            else:
                res[i] = False
        return res
        
"""
https://leetcode.cn/problems/course-schedule-iv/submissions/465655233/?envType=daily-question&envId=2023-09-12

时间
详情
96ms
击败 89.37%使用 Python3 的用户
内存
详情
18.74MB
击败 19.25%使用 Python3 的用户
"""
