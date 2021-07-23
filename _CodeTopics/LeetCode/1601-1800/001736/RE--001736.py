class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        for i in range(5):
            if time[i] == '?':
                if i == 0:
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
https://leetcode-cn.com/submissions/detail/199150277/

9 / 159 个通过测试用例
状态：执行出错

执行出错信息：
ValueError: invalid literal for int() with base 10: '?'
    if int(time[1]) < 4:
Line 11 in maximumTime (Solution.py)
    ret = Solution().maximumTime(param_1)
Line 46 in _driver (Solution.py)
    _driver()
Line 56 in <module> (Solution.py)
最后执行的输入：
"??:3?"
"""
