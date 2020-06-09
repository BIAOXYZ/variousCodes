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
            if int(numstr[:2]) > 25:
                return self.translateNum(int(numstr[2:]))
            else:
                return self.translateNum(int(numstr[1:])) + self.translateNum(int(numstr[2:]))
                
"""
# https://leetcode-cn.com/submissions/detail/77465195/

35 / 49 个通过测试用例
	状态：解答错误

输入： 624
输出： 1
预期： 2
"""
