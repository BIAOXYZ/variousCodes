import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()
        minR = 0
        for house in houses:
            ind = bisect.bisect_right(heaters, house)
            if ind == 0:
                rightHeater = heaters[0]
                minR = max(minR, rightHeater - house)
            elif ind == len(heaters):
                leftHeater = heaters[-1]
                minR = max(minR, house - leftHeater)
            else:
                leftHeater, rightHeater = heaters[ind-1], heaters[ind]
                minR = max(minR, min(house- leftHeater, rightHeater - house))
        return minR
        
"""
https://leetcode-cn.com/submissions/detail/250093744/

执行用时：64 ms, 在所有 Python 提交中击败了71.21%的用户
内存消耗：15 MB, 在所有 Python 提交中击败了54.54%的用户
通过测试用例：
30 / 30
"""
