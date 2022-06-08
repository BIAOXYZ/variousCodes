class Solution:

    def __init__(self, rects: List[List[int]]):
        self.legalX = []
        self.legalY = []
        self.minX = 10**9 + 1
        self.maxX = -10**9 - 1
        self.minY = 10**9 + 1
        self.maxY = -10**9 - 1
        for a, b, x, y in rects:
            self.legalX.append([a, x])
            self.legalY.append([b, y])
            self.minX = min(self.minX, a)
            self.maxX = max(self.maxX, x)
            self.minY = min(self.minY, b)
            self.maxY = max(self.maxY, y)

    def pick(self) -> List[int]:
        while True:
            x = random.randint(self.minX, self.maxX)
            y = random.randint(self.minX, self.maxY)
            if self.is_in_rects(x, y):
                return [x, y]
    
    def is_in_rects(self, coorX, coorY):
        for i in range(len(self.legalX)):
            a, x = self.legalX[i]
            b, y = self.legalY[i]
            if a <= coorX <= x and b <= coorY <= y:
                return True
        return False


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

"""
https://leetcode.cn/submissions/detail/323265706/

2 / 35 个通过测试用例
状态：执行出错

执行出错信息：
ValueError: empty range for randrange() (35330199, -46856949, -82187148)
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
Line 353 in randrange (/usr/lib/python3.10/random.py)
    return self.randrange(a, b+1)
Line 370 in randint (/usr/lib/python3.10/random.py)
    y = random.randint(self.minX, self.maxY)
Line 21 in pick (Solution.py)
    result = obj.pick();
Line 47 in __helper_select_method__ (Solution.py)
    ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
Line 84 in _driver (Solution.py)
    _driver()
Line 93 in <module> (Solution.py)
最后执行的输入：
["Solution","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick","pick"]
[[[[35330199,-46858448,35330694,-46856950]]],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
"""
