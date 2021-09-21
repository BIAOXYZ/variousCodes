class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        flagAlreadyMeetLetter = False
        pos = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if not flagAlreadyMeetLetter:
                    continue
                else:
                    return pos - i
            else:
                if not flagAlreadyMeetLetter:
                    flagAlreadyMeetLetter = True
                    pos = i
                else:
                    continue
        return pos + 1
        
"""
https://leetcode-cn.com/submissions/detail/221633858/

58 / 58 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.6 MB

执行用时：20 ms, 在所有 Python 提交中击败了38.14%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了5.00%的用户
"""
