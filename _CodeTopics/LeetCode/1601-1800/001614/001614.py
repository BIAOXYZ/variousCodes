class Solution:
    def maxDepth(self, s: str) -> int:

        currMaxDepth = 0
        currLeftBracket = 0
        for ch in s:
            if ch == '(':
                currLeftBracket += 1
                currMaxDepth = max(currMaxDepth, currLeftBracket)
            elif ch == ')':
                currLeftBracket -= 1
        return currMaxDepth
        
"""
https://leetcode-cn.com/submissions/detail/255787759/

执行用时：32 ms, 在所有 Python3 提交中击败了66.47%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.69%的用户
通过测试用例：
167 / 167
"""
