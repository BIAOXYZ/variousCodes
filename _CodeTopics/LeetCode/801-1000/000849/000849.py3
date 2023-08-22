class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        n = len(seats)
        occupied_indices = [i for i in range(n) if seats[i] == 1]
        
        first_occupied_ind = occupied_indices[0]
        res = first_occupied_ind - 0
        for i in range(1, len(occupied_indices)):
            # 对于中间位置的任意两个坐了人的点，最优的位置一定是两者最中间。
            curr = (occupied_indices[i] - occupied_indices[i-1]) // 2
            res = max(res, curr)
        res = max(res, n - 1 - occupied_indices[-1])
        return res
        
"""
https://leetcode.cn/problems/maximize-distance-to-closest-person/submissions/458895559/

时间
详情
48ms
击败 82.65%使用 Python3 的用户
内存
详情
16.92MB
击败 19.39%使用 Python3 的用户
"""
