class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        
        xstr = str(x)
        length = len(xstr)
        for i in range(length/2):
            if xstr[i] == xstr[length-1-i]:
                continue
            else:
                return False
        return True
        
"""
# https://leetcode-cn.com/submissions/detail/77817109/

11509 / 11509 个通过测试用例
状态：通过
执行用时：140 ms
内存消耗：12.7 MB
"""
