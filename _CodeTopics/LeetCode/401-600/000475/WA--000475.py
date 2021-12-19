import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

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
https://leetcode-cn.com/submissions/detail/250093121/

17 / 30 个通过测试用例
状态：解答错误

输入：
[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
输出：
841401046
预期结果：
161834419
"""
