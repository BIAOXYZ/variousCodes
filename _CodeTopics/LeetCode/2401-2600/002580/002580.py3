class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:

        # 以 [[1,3],[2,4], [5,7],[7,8], [10,11]] 为例：
        # 前两个区间必须在一个组；中间两个必须在一个组；最后一个单独一个组。
        # 然后每个组就是从两个“大组”里选一个（或者说从两种颜色里选一种）

        MOD = 10**9+7
        ranges.sort()
        total_group_num = 1
        curr_group_max = ranges[0][1]
        n = len(ranges)

        for i in range(1, n):
            elem_min, elem_max = ranges[i]
            # 和前一个区间有交集，此时还算一个组
            if elem_min <= curr_group_max:
                curr_group_max = max(curr_group_max, elem_max)
            else:
                total_group_num += 1
                curr_group_max = elem_max
        return (2**total_group_num) % MOD
        
"""
https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/submissions/517164837?envType=daily-question&envId=2024-03-27

通过
提交于 2024.03.27 12:53

执行用时分布
80
ms
击败
97.37%
使用 Python3 的用户
消耗内存分布
44.91
MB
击败
88.16%
使用 Python3 的用户
"""
