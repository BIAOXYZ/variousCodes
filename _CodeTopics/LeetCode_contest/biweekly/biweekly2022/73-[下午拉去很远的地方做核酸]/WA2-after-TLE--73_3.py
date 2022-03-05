from collections import defaultdict
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = [set() for _ in range(n)]
        startVertexes = set(range(n))
        vertexEdgeDict = defaultdict(list)
        for i, edge in enumerate(edges):
            if edge[1] in startVertexes:
                startVertexes.remove(edge[1])
            vertexEdgeDict[edge[0]].append(edge[1])
        
        # 肯定是慢在了每次子节点都要整个 update 集合。考虑到某个边已经用过的话，在这一次
        # 的 BFS 中就只是增加一下新的起始顶点即可。于是用一个集合来记录哪些是已经用过的 edge。
        usedEdges = set()
        
        for vertex in startVertexes:
            q = deque([vertex])
            while q:
                for i in range(len(q)):
                    currVertex = q.popleft()
                    for nextVertex in vertexEdgeDict[currVertex]:
                        if (currVertex, nextVertex) not in usedEdges:
                            res[nextVertex].add(currVertex)
                            res[nextVertex].update(res[currVertex])
                            usedEdges.add((currVertex, nextVertex))
                        else:
                            res[nextVertex].add(vertex)
                        q.append(nextVertex)
        return [sorted(list(elem)) for elem in res]
    
"""
https://leetcode-cn.com/submissions/detail/277961603/

27 / 80 个通过测试用例
状态：解答错误

输入：
6
[[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]
输出：
[[4,5],[0,2,4,5],[4],[0,1,2,4,5],[],[2,4]]
预期：
[[2,4,5],[0,2,4,5],[4],[0,1,2,4,5],[],[2,4]]
"""
