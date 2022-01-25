class DetectSquares:

    def __init__(self):
        self.dic = {}
        self.dicx = {}
        self.dicy = {}

    def add(self, point: List[int]) -> None:
        k = tuple(point)
        x, y = point[0], point[1]
        self.dic[k] = self.dic.setdefault(k, 0) + 1
        if x in self.dicx:
            self.dicx[x].add(k)
        else:
            self.dicx[x] = set([k])
        if y in self.dicy:
            self.dicy[y].add(k)
        else:
            self.dicy[y] = set([k])

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        xset = self.dicx.get(x, None)
        yset = self.dicy.get(y, None)
        if not xset or not yset:
            return 0
        ##print(f"xset is: {xset} and yset is {yset}")
        
        for samex in xset:
            if samex == tuple(point):
                continue
            newy = samex[1]
            ##print(samex, point, samex[1])
            edgeLen = abs(newy - y)
            k1, k2 = tuple([x + edgeLen, y]), tuple([x + edgeLen, newy])
            if k1 in self.dic and k2 in self.dic:
                res += self.dic[samex] * self.dic[k1] * self.dic[k2]
            k3, k4 = tuple([x - edgeLen, y]), tuple([x - edgeLen, newy])
            if k3 in self.dic and k4 in self.dic:
                res += self.dic[samex] * self.dic[k3] * self.dic[k4]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

"""
https://leetcode-cn.com/submissions/detail/262393750/

执行用时：140 ms, 在所有 Python3 提交中击败了93.67%的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了13.93%的用户
通过测试用例：
54 / 54
"""
