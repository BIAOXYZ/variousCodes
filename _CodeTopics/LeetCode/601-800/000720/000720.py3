class Solution:
    def longestWord(self, words: List[str]) -> str:

        se = set(words)
        res = ''
        for word in words:
            if all(word[0:i] in se for i in range(1, len(word))):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res
        
"""
https://leetcode-cn.com/submissions/detail/284462957/

执行用时：112 ms, 在所有 Python3 提交中击败了22.01%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了45.50%的用户
通过测试用例：
59 / 59
"""
