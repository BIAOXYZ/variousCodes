class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        
        coins.sort()
        currMax = 0
        if coins[0] != 1:
            return 1
        else:
            currMax = 1
        
        for i in range(1, len(coins)):
            if coins[i] > currMax + 1:
                break
            else:
                currMax += coins[i]
        return currMax + 1
    
"""
https://leetcode-cn.com/submissions/detail/157711472/

71 / 71 个通过测试用例
状态：通过
执行用时: 152 ms
内存消耗: 15.7 MB
"""
