class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxenergy = 1
        length = len(s)
        for i in range(length):
            currenergy = 1
            for j in range(i+1, length):
                if s[j] == s[i]:
                    currenergy += 1
                    if currenergy > maxenergy:
                        maxenergy = currenergy
                else:
                    break
        return maxenergy
    
