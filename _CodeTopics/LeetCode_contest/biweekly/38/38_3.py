class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        # 暴力估计肯定超时，但是胃不舒服实在不想想了。。。
        def is_similar(str1, str2):
            if len(str1) != len(str2):
                return False
            flag = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    flag += 1
                    if flag > 1:
                        return False
            return flag == 1
        
        res = 0
        lens, lent = len(s), len(t)
        for substrlen in range(1, lens+1):
            for inds in range(lens-substrlen+1):
                for indt in range(lent-substrlen+1):
                    if is_similar(s[inds:inds+substrlen], t[indt:indt+substrlen]):
                        res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/120046952/

63 / 63 个通过测试用例
状态：通过
执行用时: 1208 ms
内存消耗: 13 MB
"""
