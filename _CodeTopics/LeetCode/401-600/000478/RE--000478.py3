class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.rSquare = radius ** 2
        self.minX = x_center - radius
        self.maxX = x_center + radius

    def randPoint(self) -> List[float]:
        x = random.uniform(self.minX, self.maxX)
        ySquare = self.rSquare - x * x
        flag = random.randint(0, 1)
        return [x, math.sqrt(ySquare)] if flag == 1 else [x, -math.sqrt(ySquare)] 


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""
https://leetcode.cn/submissions/detail/321697959/

1 / 8 个通过测试用例
状态：执行出错

执行出错信息：
ValueError: math domain error
    return [x, math.sqrt(ySquare)] if flag == 1 else [x, -math.sqrt(ySquare)]
Line 12 in randPoint (Solution.py)
    result = obj.randPoint();
Line 28 in __helper_select_method__ (Solution.py)
    ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
Line 65 in _driver (Solution.py)
    _driver()
Line 74 in <module> (Solution.py)
最后执行的输入：
["Solution","randPoint","randPoint","randPoint"]
[[10.0,5.0,-7.5],[],[],[]]
"""
