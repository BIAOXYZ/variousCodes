class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        # 1. 两边都不等于 0，此时三点在一条直线上。
        # 2. 两边都等于 0，此时分两种情况：
        # 2.1 两边都是 x 或 y 相关的项等于 0，此时有 x0 == x1 == x2 或者 y0 == y1 == y2，
        ## 也就是三点处于和 x轴 或 y轴 平行的直线上。
        # 2.2 一边是 x 相关的项等于 0，另一边是 y 相关的项等于 0。此时要么 point0 等于 point1，
        ## 要么 point2 等于 point1（注意：point0 等于 point2 在条件 1. 里包含。）。
        if (y2 - y1) * (x1 - x0) == (y1 - y0) * (x2 - x1):
            return False
        return True
        
"""
https://leetcode.cn/submissions/detail/322827779/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
46.69%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
73.16%
的用户
通过测试用例：
206 / 206
"""
