class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 基本位运算，其实实质和普通的取模（%），然后除（/）区别不大。还没有用到（适合这道题的）位运算的高级技巧。
        res = 0
        while n > 0:
            if n & 1 != 0:
                res += 1
            n >>= 1
        return res
      
"""
https://leetcode-cn.com/submissions/detail/188947151/

601 / 601 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB

执行用时：24 ms, 在所有 Python 提交中击败了38.75%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.01%的用户
"""
