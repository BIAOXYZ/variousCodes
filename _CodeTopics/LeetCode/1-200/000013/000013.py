class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {
            "M": 1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90,
            "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1,
        }

        res = 0
        flagPass = 0
        for i, ch in enumerate(s):
            if flagPass == 1:
                flagPass = 0
                continue
            if ch not in ["C", "X", "I"]:
                res += dic[ch]
                flagPass = 0
            elif ch == "C":
                if i != len(s) - 1 and s[i+1] in ["M", "D"]:
                    res += dic[ch + s[i+1]]
                    flagPass = 1
                else:
                    res += dic[ch]
            elif ch == "X":
                if i != len(s) - 1 and s[i+1] in ["C", "L"]:
                    res += dic[ch + s[i+1]]
                    flagPass = 1
                else:
                    res += dic[ch]
            elif ch == "I":
                if i != len(s) - 1 and s[i+1] in ["X", "V"]:
                    res += dic[ch + s[i+1]]
                    flagPass = 1
                else:
                    res += dic[ch]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/177714272/

3999 / 3999 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 13 MB

执行用时：72 ms, 在所有 Python 提交中击败了40.59%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了40.12%的用户
"""
