class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 一位数一共9个，二位数一共 99-10+1 = 90 个，三位数一共 999-100+1 = 900 个。依次类推。

        if n <= 9:
            return n

        i = 0
        currLevelNumLen = i + 1
        while n >= 9 * (10**i) * currLevelNumLen:
            n -= 9 * (10**i) * currLevelNumLen
            i += 1
            currLevelNumLen += 1
           
        quotient, remainder = n / currLevelNumLen, n % currLevelNumLen
        currStartNum = 10**i
        lastNum = currStartNum + quotient
        if remainder != 0:
            return (lastNum / 10**(currLevelNumLen - remainder)) % 10
        else:
            return (lastNum - 1) % 10
        
"""
https://leetcode-cn.com/submissions/detail/243646578/

执行用时：8 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了65.45%的用户
通过测试用例：
71 / 71
"""
