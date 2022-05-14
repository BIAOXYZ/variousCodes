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
                        # https://en.wikipedia.org/wiki/Shoelace_formula
                        currArea = (x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3)
                        maxArea = max(maxArea, currArea)
        return maxArea
        
"""
https://leetcode.cn/submissions/detail/313594860/

1 / 57 个通过测试用例
状态：解答错误

输入：
[[1,0],[0,0],[0,1]]
输出：
0.00000
预期结果：
0.5
"""
