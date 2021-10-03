class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # print ord('a'), ord('z'), ord('A'), ord('Z')
        # print ord('0'), ord('9') 

        def lowercase_to_uppercase(ch):
            return chr(ord(ch) - 32)

        length = len(s)
        res = ''
        j = 1
        for i in range(length-1, -1, -1):
            ch = s[i]
            if ch == '-':
                continue
            if not ch.isdigit() and not ch.isupper():
                ch = lowercase_to_uppercase(ch)
            if j % k != 0:
                res = ch + res
            else:
                res = '-' + ch + res
            j = (j + 1) % k
        # 由于 res 可能为空，所以换一下return里的写法。
        return res[1:] if (res and res[0] == '-') else res
        
"""
https://leetcode-cn.com/submissions/detail/225523257/

38 / 38 个通过测试用例
状态：通过
执行用时: 348 ms
内存消耗: 15.2 MB

执行用时：348 ms, 在所有 Python 提交中击败了35.24%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了57.14%的用户
"""
