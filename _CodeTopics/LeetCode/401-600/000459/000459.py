class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return False
        
        length = len(s)
        indOfFirstLetter = []
        for i in range(length):
            if s[i] == s[0]:
                indOfFirstLetter.append(i)
        
        len2 = len(indOfFirstLetter)
        for i in range(1, len2/2 + 1):
            distance = indOfFirstLetter[i] - 0
            start1, start2 = 0, distance
            while start2 + distance <= length:
                if s[start1:start1+distance] == s[start2:start2+distance]:
                    start1 += distance
                    start2 += distance
                else:
                    break
            if start2 < length or start2 > length:
                continue
            else:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/101314643/

120 / 120 个通过测试用例
状态：通过
执行用时：144 ms
内存消耗：13 MB
"""
"""
执行用时：144 ms, 在所有 Python 提交中击败了32.50%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了33.75%的用户
"""
