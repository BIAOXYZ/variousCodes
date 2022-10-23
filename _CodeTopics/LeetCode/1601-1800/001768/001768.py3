class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n1, n2 = len(word1), len(word2)
        shorter, longer = min(n1, n2), max(n1, n2)
        lis = []
        for i in range(shorter):
            lis.append(word1[i])
            lis.append(word2[i])
        
        res = "".join(lis)
        if n1 > shorter:
            res += word1[shorter:]
        if n2 > shorter:
            res += word2[shorter:]
        return res
        
"""
https://leetcode.cn/submissions/detail/375665082/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
91.76%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
24.87%
的用户
通过测试用例：
108 / 108
"""
