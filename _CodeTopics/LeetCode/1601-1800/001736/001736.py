class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        for i in range(5):
            if time[i] == '?':
                if i == 0:
                    if time[1] == '?':
                        time = '23' + time[2:]
                        continue
                    if int(time[1]) < 4:
                        time = '2' + time[1:]
                    else:
                        time = '1' + time[1:]
                elif i == 1:
                    if time[0] == '2':
                        time = time[0] + '3' + time[2:]
                    else:
                        time = time[0] + '9' + time[2:]
                elif i == 3:
                    time = time[:3] + '5' + time[4]
                else:
                    time = time[:4] + '9'
        return time
        
"""
https://leetcode-cn.com/submissions/detail/199150394/

159 / 159 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了64.86%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了24.32%的用户
"""
