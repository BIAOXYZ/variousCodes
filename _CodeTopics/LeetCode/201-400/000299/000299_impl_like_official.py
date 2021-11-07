class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        
        # 官方答案 Python3 版本是下面这句，但是 f-strings 语法 Python2 不支持。
        # 于是就用 str.format() 来代替。
        # return f'{bulls}A{cows}B'
        return '{}A{}B'.format(bulls, cows)
        
"""
https://leetcode-cn.com/submissions/detail/236484932/

执行用时：36 ms, 在所有 Python 提交中击败了41.89%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了40.54%的用户
通过测试用例：
152 / 152
"""
