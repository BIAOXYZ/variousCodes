class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        flag = 0
        res = []
        tmpStr = ''
        for ch in s:
            if ch == '(':
                flag += 1
            elif ch == ')':
                flag -= 1
            tmpStr += ch
            if flag == 0:
                res.append(tmpStr[1:-1])
                tmpStr = ''
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/318885269/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
80.78%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
11.13%
的用户
通过测试用例：
59 / 59
"""
