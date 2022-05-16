class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # official
        # 又一次碰到了这个 pairwise。
        index = {c: i for i, c in enumerate(order)}
        return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))
        
"""
https://leetcode.cn/submissions/detail/314479364/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
76.76%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
77.65%
的用户
通过测试用例：
120 / 120
"""
