class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        dic = {}
        for time in times:
            if dic.has_key(time[0]):
                dic[time[0]].append(time)
            else:
                dic[time[0]] = [time]
        
        inf = float('inf')
        final = ['placeholder'] + [False for _ in range(n)]
        final[k] = True
        distance = ['placeholder'] + [inf for _ in range(n)]
        distance[k] = 0
        if not dic.has_key(k):
            return -1
        else:
            for time in dic[k]:
                v, w = time[1], time[2]
                distance[v] = w
        
        while True:
            currMin, currMinInd = inf, -1
            for i, isFinal in enumerate(final):
                if not isFinal:
                    if distance[i] < currMin:
                        currMin = distance[i]
                        currMinInd = i
            if currMinInd == -1:
                return -1
            final[currMinInd] = True
            if False not in final:
                return max(distance[1:])
            if dic.has_key(currMinInd):
                # 该部分对应 Dijkstra 最短路径算法中更新与源点的距离的步骤
                for time in dic[currMinInd]:
                    v, w = time[1], time[2]
                    distance[v] = min(distance[v], distance[currMinInd] + w)
        
"""
https://leetcode-cn.com/submissions/detail/202195354/

52 / 52 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 14.6 MB

执行用时：52 ms, 在所有 Python 提交中击败了99.44%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了45.20%的用户
"""
