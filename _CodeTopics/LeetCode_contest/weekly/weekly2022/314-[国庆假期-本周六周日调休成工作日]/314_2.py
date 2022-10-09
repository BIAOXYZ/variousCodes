class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        
        n = len(pref)
        arr = [pref[0]] + [0] * (n-1)
        currPrefixXor = pref[0]
        
        for i in range(1, n):
            arr[i] = pref[i] ^ currPrefixXor
            currPrefixXor ^= arr[i]
        return arr
    
"""
https://leetcode.cn/submissions/detail/371148009/

46 / 46 个通过测试用例
状态：通过
执行用时: 112 ms
内存消耗: 32.7 MB
"""
