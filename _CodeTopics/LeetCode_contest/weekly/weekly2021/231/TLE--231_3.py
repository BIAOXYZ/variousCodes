class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        dic = {}
        for ind, edge in enumerate(edges):
            for j in [0,1]:
                if edge[j] not in dic:
                    dic[edge[j]] = [ind]
                else:
                    dic[edge[j]].append(ind)
        
        # Dijkstra部分
        # 这还是第一次写最短路径，看print输出，跟题目条件对了一下，至少最短路径部分还是写对了的。。。
        
        inf = float("inf")
        final = ["placeholder"] + [False] * (n-1) + [True]
        distance = ["placeholder"] + [inf] * (n-1) + [0]
        for ind in dic[n]:
            edge = edges[ind]
            if edge[0] == n:
                distance[edge[1]] = edge[2]
            elif edge[1] == n:
                distance[edge[0]] = edge[2]
        
        addToFinal = 0
        while addToFinal < n-1:
            currStart = -1
            currDis = inf
            for i in range(1, len(distance)):
                dis = distance[i]
                if final[i] == False and dis < currDis:
                    currDis = dis
                    currStart = i
            final[currStart] = True
            addToFinal += 1
            for ind in dic[currStart]:
                edge = edges[ind]
                if edge[0] == currStart and final[edge[1]] == False:
                    distance[edge[1]] = min(distance[edge[1]], distance[currStart] + edge[2])
                elif edge[1] == currStart and final[edge[0]] == False:
                    distance[edge[0]] = min(distance[edge[0]], distance[currStart] + edge[2]) 
        print final, distance
        
        # DFS部分
        # 我感觉应该是用一个变种的DFS，不需要记录visited。返回的条件是只要最后到第n个节点就返回。
        
        # visited = set([])
        res = [0]
        def dfs_and_prune(v):
            if v == n:
                res[0] += 1
            # if v not in visited:
            #     visited.add(v)
            # else:
                return
            for ind in dic[v]:
                edge = edges[ind]
                if edge[0] == v and distance[edge[0]] > distance[edge[1]]:
                    dfs_and_prune(edge[1])
                elif edge[1] == v and distance[edge[1]] > distance[edge[0]]:
                    dfs_and_prune(edge[0])
        dfs_and_prune(1)
        return res[0] % (10**9+7)
    
"""
https://leetcode-cn.com/submissions/detail/152057168/

52 / 74 个通过测试用例
状态：超出时间限制
"""
