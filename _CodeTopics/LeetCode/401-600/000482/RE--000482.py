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
        return res if res[0] != '-' else res[1:]
        
"""
https://leetcode-cn.com/submissions/detail/225522681/

35 / 38 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: string index out of range
    return res if res[0] != '-' else res[1:]
Line 29 in licenseKeyFormatting (Solution.py)
    ret = Solution().licenseKeyFormatting(param_1, param_2)
Line 56 in _driver (Solution.py)
    _driver()
Line 66 in <module> (Solution.py)
最后执行的输入：
"---"
3
"""
