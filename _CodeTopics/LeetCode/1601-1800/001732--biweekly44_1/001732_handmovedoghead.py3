class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # 第 44 场双周赛第一题
        # 手动狗头题
        return max(list(itertools.accumulate(gain, initial=0)))
        
"""
https://leetcode.cn/submissions/detail/383173614/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
46.30%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
5.45%
的用户
通过测试用例：
80 / 80
"""
