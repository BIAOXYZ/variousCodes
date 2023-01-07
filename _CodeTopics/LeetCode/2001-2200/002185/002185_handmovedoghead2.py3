class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        # 手动狗头题
        return sum(map(lambda x : int(x.startswith(pref)), words))
        
"""
https://leetcode.cn/submissions/detail/393717783/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
78.39%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
34.75%
的用户
通过测试用例：
95 / 95
"""
