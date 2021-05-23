class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n = len(s)
        tmp1 = tmp0 = max1 = max0 = 0
        flag = 2
        for i in range(n):
            if s[i] == "1":
                if flag == 1:
                    tmp1 += 1
                else:
                    max0 = max(max0, tmp0)
                    flag = 1
                    tmp1 = 1
            else:
                if flag == 0:
                    tmp0 += 1
                else:
                    max1 = max(max1, tmp1)
                    flag = 0
                    tmp0 = 1
        max0, max1 = max(max0, tmp0), max(max1, tmp1)
        return max1 > max0
    
"""
https://leetcode-cn.com/submissions/detail/179988389/

137 / 137 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
