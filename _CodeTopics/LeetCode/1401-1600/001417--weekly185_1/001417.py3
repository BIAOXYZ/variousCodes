class Solution:
    def reformat(self, s: str) -> str:

        strlist, numlist = [], []
        for ch in s:
            if ch.isdigit():
                numlist.append(ch)
            else:
                strlist.append(ch)
        
        nstr, nnum = len(strlist), len(numlist)
        res = ''
        if abs(nstr - nnum) > 1:
            return res
        if nstr - nnum == 1:
            longlist, shortlist = strlist, numlist     
        else:
            longlist, shortlist = numlist, strlist
        while longlist:
            res += longlist.pop()
            if shortlist:
                res += shortlist.pop()
        return res
        
"""
https://leetcode.cn/submissions/detail/349066934/

执行用时：
52 ms
, 在所有 Python3 提交中击败了
30.63%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
18.02%
的用户
通过测试用例：
302 / 302
"""
