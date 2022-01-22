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
        for i in range(2, n, 2):
            noNeedToBuy += cost[i]
        return sum(cost) - noNeedToBuy
    
"""
https://leetcode-cn.com/submissions/detail/261341213/

19 / 192 个通过测试用例
状态：解答错误

输入：
[10,5,9,4,1,9,10,2,10,8]
输出：
42
预期：
48
"""
