class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ctr = collections.Counter(s)
        if abs(ctr["0"] - ctr["1"]) >= 2:
            return -1
        
        res = 0
        n = len(s)
        if n % 2 == 0:
            for i in range(0, n, 2):
                if s[i] != s[0]:
                    res += 1
            tmp = 0
            for i in range(0, n, 2):
                if s[i] == s[0]:
                    tmp += 1
            res = min(res, tmp)
        else:
            if ctr["0"] > ctr["1"]:
                big = "0"
            else:
                big = "1"
            for i in range(0, n, 2):
                if s[i] != big:
                    res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/177909771/

124 / 124 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB
"""
