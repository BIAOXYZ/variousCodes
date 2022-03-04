class Solution:
    def findLUSlength(self, a: str, b: str) -> int:

        # 手动狗头题（新语法糖）
        # 这个当然可以用 return -1 if a == b else max(len(a), len(b))
        ## 但这里主要是为了突出这种三个条件一行的写法。
        return -1 if a == b else len(a) if len(a) >= len(b) else len(b)
        
"""
https://leetcode-cn.com/submissions/detail/277456917/

执行用时：32 ms, 在所有 Python3 提交中击败了71.15%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.71%的用户
通过测试用例：
40 / 40
"""
