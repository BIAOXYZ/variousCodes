class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        arr.sort()
        length = len(arr)
        median = arr[(length-1)/2]
        
        absArr = []
        for i in range(length):
            absArr.append([abs(arr[i] - median), arr[i]])
            
        res = []
        absArr.sort(reverse=True)
        for i in range(k):
            res.append(absArr[i][1])
        return res
    
"""
# https://leetcode-cn.com/submissions/detail/76926141/

71 / 71 个通过测试用例
	状态：通过
执行用时：548 ms
内存消耗：33.9 MB
"""
