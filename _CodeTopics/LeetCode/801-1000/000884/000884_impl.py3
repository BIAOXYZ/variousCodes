from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        # 官方答案用到了 Counter 的相加
        freq = Counter(s1.split()) + Counter(s2.split())
        return [k for k, v in freq.items() if v == 1]
        
"""
https://leetcode-cn.com/submissions/detail/263767403/

执行用时：40 ms, 在所有 Python3 提交中击败了12.65%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了36.11%的用户
通过测试用例：55 / 55
"""
