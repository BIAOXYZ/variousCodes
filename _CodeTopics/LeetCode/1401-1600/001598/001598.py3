class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        curPos = 0
        for log in logs:
            if log == "../":
                if curPos > 0:
                    curPos -= 1
            elif log == "./":
                continue
            else:
                curPos += 1
        return 0 if curPos <= 0 else curPos
        
"""
https://leetcode.cn/submissions/detail/360886056/

执行用时：
8 ms
, 在所有 Python 提交中击败了
96.67%
的用户
内存消耗：
13 MB
, 在所有 Python 提交中击败了
96.67%
的用户
通过测试用例：
99 / 99
"""
