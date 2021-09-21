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
        
"""
https://leetcode-cn.com/submissions/detail/221632777/

49 / 58 个通过测试用例
状态：解答错误

输入：
"a"
输出：
null
预期结果：
1
"""
