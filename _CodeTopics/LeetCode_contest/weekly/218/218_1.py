class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        length = len(command)
        res = []
        flag = 'normal'
        for i in range(length):
            if flag == 'normal':
                if command[i] == '(':
                    if command[i+1] == ')':
                        flag = 'o'
                    elif command[i+1] == 'a':
                        flag = 'al'
                else:
                    res.append(command[i])
            elif flag == 'o':
                if command[i] == ')':
                    res.append('o')
                    flag = 'normal'
            else:
                if command[i] == ')':
                    flag = 'normal'
                else:
                    res.append(command[i])
        return ''.join(res)
    
"""
https://leetcode-cn.com/submissions/detail/128928149/

105 / 105 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.1 MB
"""
