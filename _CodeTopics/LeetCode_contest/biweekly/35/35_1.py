class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        length = len(arr)
        res = 0
        for currlen in range(1, length+1, 2):
            for i in range(length-currlen+1):
                for k in range(i, i+currlen):
                    res += arr[k]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/109623827/

96 / 96 个通过测试用例
状态：通过
执行用时: 100 ms
内存消耗: 12.3 MB
"""
