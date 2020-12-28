class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        
        if not arr:
            return 0
        
        length = len(arr)
        arr.sort()
        partialLen = length / 20
        newarr = arr[partialLen:length-partialLen]
        return sum(newarr) * 1.0 / len(newarr)
        
"""
https://leetcode-cn.com/submissions/detail/116498842/

50 / 50 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.3 MB
"""
