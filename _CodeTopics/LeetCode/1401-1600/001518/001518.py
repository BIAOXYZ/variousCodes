class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        currRoundFullBottleNum = numBottles
        currRoundEmptyBottleNum = 0
        total = currRoundFullBottleNum
        while currRoundFullBottleNum + currRoundEmptyBottleNum >= numExchange:
            num1 = (currRoundFullBottleNum + currRoundEmptyBottleNum) / numExchange
            num2 = (currRoundFullBottleNum + currRoundEmptyBottleNum) % numExchange
            total += num1
            currRoundFullBottleNum, currRoundEmptyBottleNum = num1, num2
        return total
        
"""
https://leetcode-cn.com/submissions/detail/249264062/

执行用时：20 ms, 在所有 Python 提交中击败了18.18%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了48.48%的用户
通过测试用例：
64 / 64
"""
