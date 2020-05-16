class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b!=0:
                a, b = b, a%b
            return a
        
        def exactN(n):
            listn = []
            for i in range(1,n):
                if gcd(i,n) == 1:
                    # listn.append("i/n") --> 这个会直接把字符串i/n加到列表里。。。。
                    s = str(i) + "/" + str(n)
                    listn.append(s)
            return listn
        
        res = []
        for i in range(2,n+1):
            res = res + exactN(i)
        return res
    
