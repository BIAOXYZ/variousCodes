class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """

        step = 0
        while s is not '1':
            if s[-1] is '0':
                s = s[:-1]
                step += 1
            else:
                if '0' not in s:
                    s = s.replace('1','0')
                    s = '1' + s
                    step += 1
                else:
                    while s[-2] != '0':
                        s = s[:-1]
                        step += 1
                    """
                    # s[-1] = '1' 又会报 TypeError: 'unicode' object does not support item assignment
                    # 只能改成直接去掉最后两位，然后字符串连接一个'1'
                    s = s[:-1]
                    s[-1] = '1'
                    """
                    s = s[:-2] + '1'
                    step += 2
        return step

"""
提交结果：超出时间限制
0 / 73 个通过测试用例
最后执行的输入： "1101"
"""
"""
# 我T你妹的LE，这TM还超时???
"""
