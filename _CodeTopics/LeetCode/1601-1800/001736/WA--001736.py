class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        for i in range(5):
            if time[i] == '?':
                if i == 0:
                    time = '2' + time[1:]
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
https://leetcode-cn.com/submissions/detail/199150188/

144 / 159 个通过测试用例
状态：解答错误

最后执行的输入：
"?4:03"
输出：
"24:03"
预期结果：
"14:03"
"""
