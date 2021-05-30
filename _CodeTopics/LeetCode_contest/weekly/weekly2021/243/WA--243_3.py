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
            for j, server in enumerate(serversSorted):
                if server[2] <= i:
                    res.append(server[1])
                    tmpserver = server[:]
                    tmpserver[2] = i + tsk
                    serversSorted.discard(server)
                    serversSorted.add(tmpserver)
                    break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/182132785/

22 / 34 个通过测试用例
状态：解答错误

最后执行的输入：
[10,63,95,16,85,57,83,95,6,29,71]
[70,31,83,15,32,67,98,65,56,48,38,90,5]
"""
