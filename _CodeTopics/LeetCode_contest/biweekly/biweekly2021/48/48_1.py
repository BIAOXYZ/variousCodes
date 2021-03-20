class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stk = [-1] * 10
        for ch in s:
            if ch.isdigit():
                stk[int(ch)] = int(ch)
        
        flag = 0
        for i in range(9, -1, -1):
            if stk[i] != -1:
                if flag == 0:
                    flag = 1
                elif flag == 1:
                    return i
        return -1
    
"""
https://leetcode-cn.com/submissions/detail/157679832/

300 / 300 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13 MB
"""
