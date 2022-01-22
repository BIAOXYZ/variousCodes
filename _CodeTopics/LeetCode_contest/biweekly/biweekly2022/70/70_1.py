class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cost.sort(reverse=True)
        n = len(cost)
        if n < 3:
            return sum(cost)
        noNeedToBuy = 0
        for i in range(2, n, 3):
            noNeedToBuy += cost[i]
        return sum(cost) - noNeedToBuy
    
"""
https://leetcode-cn.com/submissions/detail/261343785/

192 / 192 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
