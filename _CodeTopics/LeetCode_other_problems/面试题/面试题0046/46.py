class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        numstr = str(num)
        length = len(numstr)

        if length == 1:
            return 1
        elif length == 2:
            if num > 25:
                return 1
            else:
                return 2
        else:
            if int(numstr[0:2]) > 25:
                return self.translateNum(int(numstr[1:]))
            else:
                return self.translateNum(int(numstr[1:])) + self.translateNum(int(numstr[2:]))
                
"""
# https://leetcode-cn.com/submissions/detail/77481397/

49 / 49 个通过测试用例
	状态：通过
执行用时：16 ms
内存消耗：12.6 MB
"""
