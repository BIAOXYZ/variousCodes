class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        length = len(arr)
        arr.sort()
        
        dic = {}
        for i in range(1, length):
            diff = arr[i] - arr[i-1]
            if not dic.has_key(diff):
                dic[diff] = 1
            if len(dic) > 1:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/84781028/

90 / 90 个通过测试用例
	状态：通过
执行用时：8 ms
内存消耗：12.6 MB
"""
