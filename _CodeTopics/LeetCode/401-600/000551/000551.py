class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        total_A = 0
        consecutive_L = 0
        for ch in s:
            if ch == 'A':
                consecutive_L = 0
                total_A += 1
                if total_A > 1:
                    return False
            elif ch == 'L':
                consecutive_L += 1
                if consecutive_L >= 3:
                    return False
            else:
                consecutive_L = 0
        return True
        
"""
https://leetcode-cn.com/submissions/detail/207774862/

113 / 113 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.2 MB

执行用时：12 ms, 在所有 Python 提交中击败了96.67%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了11.67%的用户
"""
