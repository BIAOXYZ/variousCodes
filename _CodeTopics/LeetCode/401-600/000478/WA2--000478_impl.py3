class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.rSquare = radius * radius
        self.x_center = x_center
        self.y_center = y_center
        self.minX = x_center - radius
        self.maxX = x_center + radius
        self.minY = y_center - radius
        self.maxY = y_center + radius

    def randPoint(self) -> List[float]:
        # 没明白为啥之前那个每次保证从合法的集合里随机抽怎么就不对了。。。
        # 但是依稀想起之前做的拒绝采样题的影子，好像是不对。回头看看吧。
        while True:
            x = random.uniform(self.minX, self.maxX)
            y = random.uniform(self.minY, self.maxY)
            if x**2 + y**2 <= self.rSquare:
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""
https://leetcode.cn/submissions/detail/321698979/

3 / 8 个通过测试用例
状态：解答错误

最后执行的输入：
["Solution","randPoint","randPoint","randPoint","randPoint","randPoint","randPoint","randPoint","randPoint","randPoint","randPoint"]
[[100.0,25.0,30],[],[],[],[],[],[],[],[],[],[]]
"""
"""
服了，这道题有病吧。。。
"""
