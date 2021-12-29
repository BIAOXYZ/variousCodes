from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        length = len(hand)
        if length % groupSize != 0:
            return False
        
        ctr = Counter(hand)
        while ctr:
            currMin = min(ctr.keys())
            ctr[currMin] -= 1
            if ctr[currMin] == 0:
                del ctr[currMin]
            for i in range(groupSize-1):
                currMin += 1
                if currMin in ctr:
                    ctr[currMin] -= 1
                    if ctr[currMin] == 0:
                        del ctr[currMin]
                else:
                    return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/253319626/

执行用时：560 ms, 在所有 Python 提交中击败了35.29%的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了17.65%的用户
通过测试用例：
73 / 73
"""
