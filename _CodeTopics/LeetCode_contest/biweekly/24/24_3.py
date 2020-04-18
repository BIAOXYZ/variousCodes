class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        # 所谓开心字符串就是相邻两个位置不相等的字符串，且只能是a,b,c
        # 那么最大的“组”里的字符串数是2^(n-1)，比如都是3位长的话，第一大组是"aba", "abc", "aca", "acb"
        
        if k < 1:
            return ""
        if k > 3*(2**(n-1)):
            return ""
        
        resStr = ""
        if k <= 2**(n-1):
            resStr = resStr + 'a'
            k -= 0*(2**(n-1))
            n -= 1
        elif 2**(n-1) < k <= 2*(2**(n-1)):
            resStr = resStr + 'b'
            k -= 1*(2**(n-1))
            n -= 1
        else:
            resStr = resStr + 'c'
            k -= 2*(2**(n-1))
            n -= 1
        
        while n > 0:
            if k <= 2**(n-1):
                if resStr[-1] == 'a':
                    # 本来想用如下形式的，但是还是没法合到一起，所以又回归用字母判断的chuo办法。。。
                    # resStr = resStr + chr(ord(resStr[-1]) + 1) 
                    resStr = resStr + 'b'
                else:
                    resStr = resStr + 'a'
            else:
                if resStr[-1] == 'c':
                    resStr = resStr + 'b'
                else:
                    resStr = resStr + 'c'
                k -= 2**(n-1)
            n -= 1
        return resStr
         
