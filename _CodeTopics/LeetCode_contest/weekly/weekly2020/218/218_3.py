class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 终于感受到了python的优势。。。
        # 这题比赛时候leetcode抽风了半小时，佛了。。。
        tmpstr = ''
        for i in range(1, n+1):
            tmpstr += str(bin(i))[2:]
        return int(tmpstr, 2) % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/128952296/

403 / 403 个通过测试用例
状态：通过
执行用时: 1612 ms
内存消耗: 18.4 MB
"""
