class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        length = len(candiesCount)
        prefixSum = [candiesCount[0]]
        for i in range(1, length):
            prefixSum.append(prefixSum[-1] + candiesCount[i])
        
        res = []
        for query in queries:
            typeIndex, day, limit = query[0], query[1], query[2]
            maxEat = (day+1) * limit
            minEat = day * 1
            if typeIndex == 0:
                if minEat >= prefixSum[typeIndex]:
                    res.append(False)
                else:
                    res.append(True)
            else:
                if maxEat <= prefixSum[typeIndex-1] or minEat >= prefixSum[typeIndex]:
                    res.append(False)
                else:
                    res.append(True)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/142496014/

62 / 62 个通过测试用例
状态：通过
执行用时: 208 ms
内存消耗: 49.9 MB
"""
