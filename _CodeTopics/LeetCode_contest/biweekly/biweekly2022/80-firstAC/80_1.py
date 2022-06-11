class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        
        if len(password) < 8:
            return False
        alphabeta = [chr(i) for i in range(ord('a'), ord('z')+1)]
        if all(ch not in password for ch in alphabeta):
            return False
        Alphabeta = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        if all(ch not in password for ch in Alphabeta):
            return False
        if all(ch not in password for ch in "0123456789"):
            return False
        if all(ch not in password for ch in "!@#$%^&*()-+"):
            return False
        pre = password[0]
        for i in range(1, len(password)):
            if password[i] == pre:
                return False
            else:
                pre = password[i]
        return True
    
"""
https://leetcode.cn/submissions/detail/324207897/

148 / 148 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB
"""
