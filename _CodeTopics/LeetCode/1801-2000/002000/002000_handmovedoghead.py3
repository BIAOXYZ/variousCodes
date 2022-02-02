class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # 手动狗头题
        return ''.join(reversed(word[:word.index(ch)+1])) + word[word.index(ch)+1:] if ch in word else word
        
"""
https://leetcode-cn.com/submissions/detail/264259956/

执行用时：40 ms, 在所有 Python3 提交中击败了9.37%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.00%的用户
通过测试用例：
112 / 112
"""
