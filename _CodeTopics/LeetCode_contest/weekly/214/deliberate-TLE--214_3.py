class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        
        # 测试用例最后一个已经发现会超时了，故只是提交下而已。
        value = 0
        while orders > 0:
            currMax = max(inventory)
            value += currMax
            value %= 1000000007
            ind = inventory.index(currMax)
            inventory[ind] -= 1
            orders -= 1
        return value
    
"""
https://leetcode-cn.com/submissions/detail/121825941/

3 / 94 个通过测试用例
状态：超出时间限制

最后执行的输入：
[1000000000]
1000000000
"""
