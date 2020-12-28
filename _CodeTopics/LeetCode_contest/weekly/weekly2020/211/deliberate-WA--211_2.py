class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        
        def minstring(arr, a):
            length = len(arr) 
            if a % 2 == 1:
                tmp = arr[0]
            else:
                if arr[0] % 2 == 1:
                    tmp = arr[0] - 1
                else:
                    tmp = arr[0]
            for i in range(length):
                arr[i] = str((int(arr[i]) - int(tmp)) % 10)
            return arr
        
        length = len(s)
        if b % 2 == 1:
            round = length
        else:
            round = length/2
        
        res = s
        for k in range(1, round+1):
            newstr = ["a"] * length
            for i in range(length):
                pos = (i + k*b) % length
                newstr[pos] = s[i]
            newlist = minstring(newstr, a)
            res = min(s, "".join(newlist))
        return res
    
"""
https://leetcode-cn.com/submissions/detail/116607326/

0 / 80 个通过测试用例
状态：解答错误

输入：
"5525"
9
2
输出：
"0070"
预期：
"2050"
"""
