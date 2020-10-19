class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True

        revertednum = 0
        while x > revertednum:
            revertednum = revertednum * 10 + x % 10
            # 输入x的位数为奇数时得有这个条件。而且这个条件得在 x = x / 10之前。
            # 例如131，第一轮后x变为13，revertednum变为1。
            # 下一轮到注释这里的时候，revertednum变为13就得去和x比较了，否则就晚了。
            if revertednum == x:
                return True
            x = x / 10
        
        if x == revertednum:
            return True
        else:    
            return False
            
"""
https://leetcode-cn.com/submissions/detail/77846998/

11504 / 11509 个通过测试用例
状态：解答错误

输入：10
输出：true
预期：false
"""
