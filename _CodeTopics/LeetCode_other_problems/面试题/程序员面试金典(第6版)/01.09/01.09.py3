class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        
        n1, n2 = len(s1), len(s2)
        if n1 != n2:
            return False
        if n1 == 0:
            return True
        
        ch = s1[0]
        for i in range(n2):
            if s2[i] == ch:
                if s2[i:] + s2[:i] == s1:
                    return True
        return False
        
"""
https://leetcode.cn/submissions/detail/368305624/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
31.02%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
92.71%
的用户
通过测试用例：
31 / 31
"""
