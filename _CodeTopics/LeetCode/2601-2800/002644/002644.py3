class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        def calculate_score(divisor):
            return sum(1 for num in nums if num % divisor == 0)

        scores = list(map(calculate_score, divisors))
        zipped = list(zip(scores, divisors))
        # or:
        # zipped = sorted(zipped, key = lambda x : (-x[0], x[1]))
        zipped.sort(key = lambda x : (-x[0], x[1]))
        return zipped[0][1]
        
"""
https://leetcode.cn/problems/find-the-maximum-divisibility-score/submissions/532952474

通过
提交于 2024.05.18 22:30

执行用时分布
2666
ms
击败
40.14%
使用 Python3 的用户
消耗内存分布
16.75
MB
击败
6.34%
使用 Python3 的用户
"""
