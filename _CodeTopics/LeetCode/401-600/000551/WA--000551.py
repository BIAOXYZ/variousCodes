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
https://leetcode-cn.com/submissions/detail/207771265/

111 / 113 个通过测试用例
状态：解答错误

最后执行的输入：
"LALL"
输出：
false
预期结果：
true
"""
