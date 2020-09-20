class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        
        length = len(text)
        whitespaceNum = 0
        word = []
        whflag, tmpword = False, ''
        if text[0] == ' ':
            whflag = True
            whitespaceNum += 1
        else:
            whflag = False
            tmpword += text[0]
        
        for i in range(1,length):
            if whflag:
                if text[i] == ' ':
                    whitespaceNum += 1
                else:
                    whflag = False
                    tmpword += text[i]
            else:
                if text[i] == ' ':
                    whflag = True
                    whitespaceNum += 1
                    word.append(tmpword)
                    tmpword = ''
                else:
                    tmpword += text[i]
        # 最后如果是字母结尾，还得把这个tmpword给append进去。
        if whflag == False:
            word.append(tmpword)
        
        lenw = len(word)
        if lenw == 1:
            for i in range(whitespaceNum):
                word[0] += ' '
            return word[0]
        
        quo, rem = whitespaceNum / (lenw-1), whitespaceNum % (lenw-1)
        for i in range(lenw-1):
            for j in range(quo):
                word[i] += ' '
        for j in range(rem):
            word[-1] += ' '
        return ''.join(word)
    
"""
https://leetcode-cn.com/submissions/detail/109733879/

88 / 88 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.4 MB
"""
