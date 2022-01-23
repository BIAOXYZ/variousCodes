from sortedcontainers import SortedList
class StockPrice:

    # 第 262 场周赛第三题：
    # https://leetcode-cn.com/submissions/detail/227352600/
    # 比赛时超时是因为对于 current/maximum/minimum 这三类查询，
    # 每次就是trivial的遍历，所以总的算下来是 O(n^2)，10^5 的输入当然就超时了。

    def __init__(self):
        self.stockDic = {}
        self.latestKey = -1
        self.onlyPrices = SortedList([])

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latestKey:
            self.latestKey = timestamp
        # 下面这个 if else 可以写的更简练点，但是故意这样写，更清楚。
        if timestamp not in self.stockDic:
            self.stockDic[timestamp] = price
            self.onlyPrices.add(price)
        else:
            oldValue = self.stockDic[timestamp]
            self.onlyPrices.remove(oldValue)
            self.stockDic[timestamp] = price
            self.onlyPrices.add(price)
        ## print(self.stockDic, self.onlyPrices)

    def current(self) -> int:
        return self.stockDic[self.latestKey]

    def maximum(self) -> int:
        return self.onlyPrices[-1]

    def minimum(self) -> int:
        return self.onlyPrices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

"""
https://leetcode-cn.com/submissions/detail/261642604/

执行用时：700 ms, 在所有 Python3 提交中击败了53.93%的用户
内存消耗：51.8 MB, 在所有 Python3 提交中击败了92.15%的用户
通过测试用例：
18 / 18
"""
