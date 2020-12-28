class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        
        def isprefix(w1, w2):
            len1 = len(w1)
            len2 = len(w2)
            if len2 < len1:
                return False
            for i in range(len1):
                if w1[i] == w2[i]:
                    continue
                else:
                    return False
            return True
        
        wordlist = []
        currword = ''
        for i in range(len(sentence)):
            # 妈蛋，这里又吃了空字符''和空格字符' '的亏。。。
            if sentence[i] != ' ':
                ###print i,sentence[i]
                currword = currword + sentence[i]
                ###print "currword = %s" % (currword)
                ###print "\n"
            else:
                wordlist.append(currword)
                ###print "wordlist = %s" % (wordlist)
                currword = ''
        # 因为如果不是空格结尾，最后还有个单词在前面append进去。。。
        if sentence[-1] != ' ':
            wordlist.append(currword)
        
        for i in range(len(wordlist)):
            if isprefix(searchWord,wordlist[i]):
                return i + 1
        return -1
    
"""
# https://leetcode-cn.com/contest/weekly-contest-190/submissions/detail/73185774/
"""
