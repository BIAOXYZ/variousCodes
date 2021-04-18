class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        
        length = len(tasks)
        newtasks = [[tasks[i][0], tasks[i][1], i] for i in range(length)]
        newtasks.sort(reverse=True)
        ##print newtasks
        
        nextStartTime = newtasks[-1][0] + newtasks[-1][1]
        res = [newtasks[-1][2]]
        currAvailable = []
        heapq.heapify(currAvailable)
        newtasks.pop()
        while currAvailable or newtasks:
            for i in range(len(newtasks)-1, -1, -1):
                if newtasks[i][0] <= nextStartTime:
                    tmp = [newtasks[i][1], newtasks[i][2], newtasks[i][0]]
                    heapq.heappush(currAvailable, tmp)
                    newtasks.remove(newtasks[i])
            if currAvailable:
                tmp = heapq.heappop(currAvailable)
                res.append(tmp[1])
                nextStartTime += tmp[0]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/169182510/

28 / 34 个通过测试用例
状态：超出时间限制
"""
