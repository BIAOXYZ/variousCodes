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
        
        value = 0
        for i in range(length):
            value += inventory[i] * (inventory[i]+1) / 2
        
        negvalue = 0
        currMultiplier = 1
        while leftball >= length:
            negvalue += currMultiplier * length
            leftball -= length; currMultiplier += 1
        negvalue += currMultiplier * leftball
        
        return (value - negvalue) % 1000000007
    
"""
https://leetcode-cn.com/submissions/detail/121833035/

7 / 94 个通过测试用例
状态：超出时间限制

最后执行的输入：
[773160767]
252264991
"""
