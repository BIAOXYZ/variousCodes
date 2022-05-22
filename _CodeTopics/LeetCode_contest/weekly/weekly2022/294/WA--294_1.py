class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        
        if letter not in s:
            return 0
        res = s.count(letter) * 1.0 / len(s)
        return int(round(res * 100))
    
"""
https://leetcode.cn/submissions/detail/316518145/

77 / 85 个通过测试用例
状态：解答错误

输入：
"sgawtb"
"s"
输出：
17
预期：
16
"""
