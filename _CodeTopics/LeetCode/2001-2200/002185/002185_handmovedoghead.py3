class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        # 手动狗头题
        return sum([1 if word.startswith(pref) else 0 for word in words])
        
"""
https://leetcode.cn/submissions/detail/393717396/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
93.22%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
17.80%
的用户
通过测试用例：
95 / 95
"""
