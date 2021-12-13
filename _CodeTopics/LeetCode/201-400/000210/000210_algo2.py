import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        inDegree = [0 for i in range(numCourses)]
        res = []
        
        edges = collections.defaultdict(list)
        for info in prerequisites:
            edges[info[1]].append(info[0])
            inDegree[info[0]] += 1
        
        q = collections.deque([vertex for vertex in range(numCourses) if inDegree[vertex] == 0])
        while q:
            currVertex = q.popleft()
            res.append(currVertex)
            for dependentVertex in edges[currVertex]:
                inDegree[dependentVertex] -= 1
                if inDegree[dependentVertex] == 0:
                    q.append(dependentVertex)
        
        return [] if len(res) != numCourses else res
        
"""
https://leetcode-cn.com/submissions/detail/248245648/

执行用时：24 ms, 在所有 Python 提交中击败了77.53%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了25.84%的用户
通过测试用例：
44 / 44
"""
