class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        ddic = defaultdict(list)
        for i, ch in enumerate(s):
            ddic[ch].append(i)
        return all(v[1] - v[0] - 1 == distance[ord(k) - ord('a')] for k, v in ddic.items())
        
"""
https://leetcode.cn/submissions/detail/422817458/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
65.06%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
90.36%
的用户
通过测试用例：
335 / 335
"""
