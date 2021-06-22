class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = 0
        while n > 0:
            if n % 2 != 0:
                res += 1
            n /= 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/188947038/

601 / 601 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.1 MB

执行用时：12 ms, 在所有 Python 提交中击败了95.18%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了22.68%的用户
"""
