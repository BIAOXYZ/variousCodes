class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = [1, 0]   
        for letter in s:
            if letter == 'A':
                res[0] = 2 * res[0] + res[1]
            else:
                res[1] = 2 * res[1] + res[0]
        return res[0] + res[1]
    
"""
https://leetcode-cn.com/contest/season/2020-fall/submissions/107257570/
"""
