class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def process_email(email):
            res = ''
            omitFlag = False
            afterAtFlag = False
            for ch in email:
                if ch == '@':
                    afterAtFlag = True
                    res += ch
                elif ch == '+':
                    omitFlag = True
                elif ch == '.':
                    if afterAtFlag:
                        res += ch
                else:
                    if afterAtFlag or not omitFlag:
                        res += ch
            return res
        
        se = set()
        for email in emails:
            se.add(process_email(email))
        return len(se)
        
"""
https://leetcode.cn/submissions/detail/321386438/

执行用时：
76 ms
, 在所有 Python3 提交中击败了
5.74%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
10.97%
的用户
通过测试用例：
185 / 185
"""
