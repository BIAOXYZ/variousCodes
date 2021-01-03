class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        res = 0
        
        for i in range(len(boxTypes)):
            if truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                res += boxTypes[i][0] * boxTypes[i][1]
            else:
                res += truckSize * boxTypes[i][1]
                break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/135536963/

75 / 75 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.4 MB
"""
