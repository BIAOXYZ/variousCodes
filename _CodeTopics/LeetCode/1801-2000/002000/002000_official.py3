class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # 官方答案，好处是不需要用 if 判断一下。
        i = word.find(ch) + 1
        return word[:i][::-1] + word[i:]
        
"""
https://leetcode-cn.com/submissions/detail/264303606/

执行用时：40 ms, 在所有 Python3 提交中击败了9.37%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了37.24%的用户
通过测试用例：
112 / 112
"""
