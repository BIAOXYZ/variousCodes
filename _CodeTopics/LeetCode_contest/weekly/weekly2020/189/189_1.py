class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        
        res = 0
        length = len(startTime)
        
        for i in range(length):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                res += 1
        return res
    
"""
111 / 111 个通过测试用例
	状态：通过
执行用时：24 ms
内存消耗：12.6 MB
"""
