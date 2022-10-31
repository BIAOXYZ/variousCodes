class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        # 手动狗头题
        return ''.join(word1) == ''.join(word2)
        
"""
https://leetcode.cn/submissions/detail/378224600/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
87.95%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
35.62%
的用户
通过测试用例：
110 / 110
"""
