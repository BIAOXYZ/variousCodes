class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        
        length = len(inventory)
        totalball = sum(inventory)
        leftball = totalball - orders
        #avgleftball = leftball / length
        
        if length == 1:
            if orders == 1:
                return inventory[0]
            else:
                return ((inventory[0] + inventory[0] - orders + 1) * orders / 2) % 1000000007
        
        value = 0
        for i in range(length):
            value += inventory[i] * (inventory[i]+1) / 2
            if value > 1000000007:
                value %= 1000000007
        
        negvalue = 0
        currMultiplier = 1
        while leftball >= length:
            negvalue += currMultiplier * length
            leftball -= length; currMultiplier += 1
        negvalue += currMultiplier * leftball
        if negvalue > 1000000007:
            negvalue %= 1000000007
        return (value + 1000000007 - negvalue) % 1000000007
    
"""
https://leetcode-cn.com/submissions/detail/121835816/

9 / 94 个通过测试用例
状态：超出时间限制

最后执行的输入：
[497978859,167261111,483575207,591815159]
836556809
"""
