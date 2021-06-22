class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 位运算的高级技巧。
        res = 0
        while n > 0:
            n &= n - 1
            res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/188947211/

601 / 601 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.9 MB

执行用时：12 ms, 在所有 Python 提交中击败了95.18%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了53.40%的用户
"""
