class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        # 和前面那个 `https://leetcode-cn.com/submissions/detail/250847461/` 相比差别不大。
        # 就是找匹配的起始位置上一个用遍历，这个 .find() 方法。

        lena, lenb = len(a), len(b)
        quotient, remainder = lenb / lena, lenb % lena
        if remainder == 0:
            quotient = quotient + 1
        else:
            quotient = quotient + 2
        A = a * quotient
        
        ind = A.find(b)
        if ind == -1:
            return -1
        return quotient - 1 if len(A) - (ind + lenb) >= lena else quotient
        
"""
https://leetcode-cn.com/submissions/detail/250848404/

执行用时：76 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了39.02%的用户
通过测试用例：
57 / 57
"""
