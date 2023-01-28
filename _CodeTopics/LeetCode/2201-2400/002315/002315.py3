class Solution:
    def countAsterisks(self, s: str) -> int:

        flag = 1
        res = 0
        for ch in s:
            if ch == '|':
                flag ^= 1
            elif ch == '*':
                if flag:
                    res += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/397623675/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
92.99%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
6.75%
的用户
通过测试用例：
69 / 69
"""
