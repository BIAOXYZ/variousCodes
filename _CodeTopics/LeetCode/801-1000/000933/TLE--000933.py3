class RecentCounter:

    def __init__(self):
        self.se = set()

    def ping(self, t: int) -> int:
        self.se.add(t)
        return sum(time in self.se for time in range(max(0, t-3000), t+1))


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
https://leetcode-cn.com/submissions/detail/309729713/

64 / 68 个通过测试用例
状态：超出时间限制
"""
