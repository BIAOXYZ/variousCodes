class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stk = []
        for ch in s:
            if not stk:
                stk.append(ch)
            else:
                if stk[-1] == "[" and ch == "]":
                    stk.pop()
                else:
                    stk.append(ch)
        tmp = len(stk) / 2
        return tmp / 2 if tmp % 2 == 0 else (tmp + 1) / 2
    
"""
https://leetcode-cn.com/submissions/detail/204528413/

58 / 58 个通过测试用例
状态：通过
执行用时: 640 ms
内存消耗: 32.4 MB
"""
