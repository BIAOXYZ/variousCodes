class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        
        changeNum = 0
        for i, dig in enumerate(num):
            digit = int(dig)
            if changeNum == 0:
                if change[digit] > digit:
                    changeNum = 1
                    num = num[:i] + str(change[digit]) + num[i+1:]
            elif changeNum == 1:
                if change[digit] > digit:
                    num = num[:i] + str(change[digit]) + num[i+1:]
                elif change[digit] == digit:
                    continue
                else:
                    break
        return num
    
"""
https://leetcode-cn.com/submissions/detail/199515312/

279 / 279 个通过测试用例
状态：通过
执行用时: 6456 ms
内存消耗: 15.6 MB
"""
