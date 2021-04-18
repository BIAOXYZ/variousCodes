class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        
        costs.sort()
        res = 0
        for cost in costs:
            if cost <= coins:
                res += 1
                coins -= cost
            else:
                break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/169129397/

61 / 61 个通过测试用例
状态：通过
执行用时: 204 ms
内存消耗: 21.2 MB
"""
