class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        n = len(points)
        maxArea = 0
        for i in range(n-2):
            x1, y1 = points[i]
            for j in range(i+1, n-1):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    if (y1 - y2) * (x2 - x3) != (y2 - y3) * (x1 - x2):
                        print("....")
                        # https://en.wikipedia.org/wiki/Shoelace_formula
                        currArea = abs( (x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3) ) / 2
                        maxArea = max(maxArea, currArea)
        return maxArea
        
"""
https://leetcode.cn/submissions/detail/313595445/

执行用时：
208 ms
, 在所有 Python3 提交中击败了
33.64%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
39.39%
的用户
通过测试用例：
57 / 57
"""
