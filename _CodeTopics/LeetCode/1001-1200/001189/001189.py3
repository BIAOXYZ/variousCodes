from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        ctr = Counter(text)
        return min(ctr['a'], ctr['b'], ctr['l']//2, ctr['n'], ctr['o']//2)
        
"""
https://leetcode-cn.com/submissions/detail/267619988/

执行用时：40 ms, 在所有 Python3 提交中击败了32.13%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.04%的用户
通过测试用例：
25 / 25
"""
