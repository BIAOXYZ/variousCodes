class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = len(s)
        newstr = ''
        for i in range(length):
            if (ord('0') <= ord(s[i]) and ord('9') >= ord(s[i])) or \
                (ord('a') <= ord(s[i]) and ord('z') >= ord(s[i])):
                newstr = newstr + s[i]
            elif (ord('A') <= ord(s[i]) and ord('Z') >= ord(s[i])):
                newstr = newstr + chr(ord(s[i]) + 32)
        
        # 不论奇数还是偶数都是这个值，简单试试长度为4和长度为5就知道了。
        newlength = len(newstr)
        for i in range(newlength/2):
            if newstr[i] != newstr[newlength-1-i]:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/80213190/

476 / 476 个通过测试用例
状态：通过
执行用时：572 ms
内存消耗：17.4 MB
"""
