class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        letterlist = []
        numberlist = []
        res = ''
        
        for i in range(len(s)):
            if s[i].isalpha():
                letterlist.append(s[i])
            # 此时s[i].isdight()为True
            else:
                numberlist.append(s[i])
        
        # 这次发现可以在leetcode做题的界面直接加打印来debug~
        #print letterlist
        #print numberlist
        
        if abs(len(letterlist) - len(numberlist)) > 1:
            return ''
        elif len(letterlist) > len(numberlist):
            res = res + letterlist[0]
            for i in range(len(numberlist)):
                res = res + numberlist[i] + letterlist[i+1]
        elif len(letterlist) < len(numberlist):
            res = res + numberlist[0]
            for i in range(len(letterlist)):
                res = res + letterlist[i] + numberlist[i+1]
        else:
            for i in range(len(numberlist)):
                res = res + letterlist[i] + numberlist[i]
        return res
    
