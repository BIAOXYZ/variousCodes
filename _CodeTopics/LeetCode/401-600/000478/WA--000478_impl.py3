class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.rSquare = radius * radius
        self.x_center = x_center
        self.y_center = y_center
        self.minX = x_center - radius
        self.maxX = x_center + radius

    def randPoint(self) -> List[float]:
        x = random.uniform(self.minX, self.maxX)
        ySquare = self.rSquare - (x - self.x_center)**2
        maxY = self.y_center + math.sqrt(ySquare)
        minY = self.y_center - math.sqrt(ySquare)
        return [x, random.uniform(minY, maxY)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""
https://leetcode.cn/submissions/detail/321698507/

7 / 8 个通过测试用例
状态：解答错误
"""
