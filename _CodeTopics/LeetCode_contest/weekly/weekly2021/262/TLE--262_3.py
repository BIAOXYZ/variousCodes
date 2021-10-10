class StockPrice(object):

    def __init__(self):
        self.d = {}
        

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.d[timestamp] = price
        
        
    def current(self):
        """
        :rtype: int
        """
        latest = max(self.d.keys())
        return self.d[latest]
        

    def maximum(self):
        """
        :rtype: int
        """
        return max(self.d.values())


    def minimum(self):
        """
        :rtype: int
        """
        return min(self.d.values())


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

"""
https://leetcode-cn.com/submissions/detail/227352600/

9 / 17 个通过测试用例
状态：超出时间限制
"""
