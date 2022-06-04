class Solution:

    # 服了这破题了，看评论区有人问意义在哪，本来也不觉得。这TM我现在也烦了。。。这题意义在哪？？？

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [self.xc + x, self.yc + y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""
https://leetcode.cn/submissions/detail/321699104/

执行用时：
164 ms
, 在所有 Python3 提交中击败了
62.39%
的用户
内存消耗：
24.8 MB
, 在所有 Python3 提交中击败了
81.42%
的用户
通过测试用例：
8 / 8
"""
