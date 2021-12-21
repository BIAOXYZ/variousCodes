class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        # 重复若干次 a 得到 A， A 只需要比 b 长出来一个 a 还多一点就可以了。其实就类似周期性，比如：
        # abcdabcdabcd
        # cdabcdab
        #  cdabcdab
        #   cdabcdab
        # 字符串 b 中的首字母分别和 a 的各个字母对齐，然后只要保证大 A 比较长，让 b 比的时候用不完即可。

        lena, lenb = len(a), len(b)
        quotient, remainder = lenb / lena, lenb % lena
        if remainder == 0:
            quotient = quotient + 1
        else:
            quotient = quotient + 2
        A = a * quotient
        
        for start in range(lena):
            if A[start:start + lenb] == b:
                return quotient - 1 if len(A) - (start + lenb) >= lena else quotient
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/250847461/

执行用时：84 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了7.32%的用户
通过测试用例：
57 / 57
"""
