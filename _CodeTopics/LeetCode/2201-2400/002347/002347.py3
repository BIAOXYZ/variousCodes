class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        if len(set(suits)) == 1:
            return "Flush"
        elif max(Counter(ranks).values()) >= 3:
            return "Three of a Kind"
        elif max(Counter(ranks).values()) == 2:
            return "Pair"
        else:
            return "High Card"
        
"""
https://leetcode.cn/submissions/detail/404382213/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
90.85%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
93.46%
的用户
通过测试用例：
98 / 98
"""
