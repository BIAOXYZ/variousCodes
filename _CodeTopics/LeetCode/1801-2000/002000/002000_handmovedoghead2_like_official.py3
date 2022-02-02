class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # 手动狗头题
        # 类似官方答案，不过还是需要用 if 判断一下。
        return word[word.find(ch)::-1] + word[word.find(ch)+1:] if word.find(ch) != -1 else word
        
"""
https://leetcode-cn.com/submissions/detail/264301771/

执行用时：36 ms, 在所有 Python3 提交中击败了34.19%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了64.17%的用户
通过测试用例：
112 / 112
"""
