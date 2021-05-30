from sortedcontainers import SortedList
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        
        n, m = len(servers), len(tasks)
        serversSorted = SortedList([[servers[i], i, 0] for i in range(n)])
        
        res = []
        for i in range(m):
            tsk = tasks[i]
            found = 0
            minServerAvaiTime = float('inf')
            for j, server in enumerate(serversSorted):
                if server[2] < minServerAvaiTime:
                    minServerAvaiTime = server[2]
                    candidateServer = server[:]
                if server[2] <= i:
                    found = 1
                    res.append(server[1])
                    tmpserver = server[:]
                    tmpserver[2] = i + tsk
                    serversSorted.discard(server)
                    serversSorted.add(tmpserver)
                    break
            # 上一个错就是没考虑万一当前服务器都不可用怎么办——只能等到最近的那个candidate服务器可用了
            if not found:
                res.append(candidateServer[1])
                tmpserver = candidateServer[:]
                tmpserver[2] = i + tsk
                serversSorted.discard(candidateServer)
                serversSorted.add(tmpserver)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/182141617/

22 / 34 个通过测试用例
状态：解答错误

最后执行的输入：
[31,96,73,90,15,11,1,90,72,9,30,88]
[87,10,3,5,76,74,38,64,16,64,93,95,60,79,54,26,30,44,64,71]
"""
