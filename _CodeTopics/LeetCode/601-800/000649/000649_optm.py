class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        length = len(senate)
        lisR, lisD = [], []
        for i in range(len(senate)):
            if senate[i] == "R":
                lisR.append(i)
            else:
                lisD.append(i)
        
        while lisR and lisD:
            if lisR[0] < lisD[0]:
                lisR.append(lisR[0] + length)
            else:
                lisD.append(lisD[0] + length)
            lisR.pop(0)
            lisD.pop(0)
        return "Radiant" if lisR else "Dire"
        
"""
https://leetcode-cn.com/submissions/detail/130411997/

81 / 81 个通过测试用例
状态：通过
执行用时: 112 ms
内存消耗: 13.5 MB

执行用时：112 ms, 在所有 Python 提交中击败了70.00%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了30.00%的用户
"""
