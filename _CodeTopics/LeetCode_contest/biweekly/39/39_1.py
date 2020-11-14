class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        length = len(code)
        res = [0] * length
        
        if k == 0:
            return res
        elif k > 0:
            for i in range(length):
                for offset in range(1,k+1):
                    res[i] += code[(i + offset) % length]
        else:
            for i in range(length):
                for offset in range(-1,k-1,-1):
                    res[i] += code[(i + offset) % length]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/123458508/

74 / 74 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13 MB
"""
