class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        
        costs.sort()
        i = 0
        while i <= len(costs) - 1 and coins >= costs[i]:
            coins -= costs[i]
            i += 1
        return i
        
"""
https://leetcode-cn.com/submissions/detail/191506539/

63 / 63 个通过测试用例
状态：通过
执行用时: 180 ms
内存消耗: 21.1 MB

执行用时：180 ms, 在所有 Python 提交中击败了54.58%的用户
内存消耗：21.1 MB, 在所有 Python 提交中击败了74.30%的用户
"""
