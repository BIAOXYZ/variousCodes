class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        def isVowel(ch):
            if ch in 'aeiou':
                return True
            else:
                return False

        length = len(s)
        maxVowel = currVowel = 0
        firstWord = s[:k]
        for i in range(k):
            if isVowel(firstWord[i]):
                currVowel += 1
            if currVowel == k:
                return k
        if currVowel > maxVowel:
            maxVowel = currVowel
        
        for i in range(1,length-k+1):
            currWord = s[i:i+k]
            if isVowel(s[i-1]) == isVowel(currWord[k-1]):
                continue
            else:
                if isVowel(s[i-1]) == False and isVowel(currWord[k-1]) == True:
                    currVowel += 1
                    if currVowel > maxVowel:
                        maxVowel = currVowel
                else:
                    currVowel -= 1
        return maxVowel
    
"""
# https://leetcode-cn.com/contest/weekly-contest-190/submissions/detail/73202897/

# 哎哟，刚才前面190_1和TLE--190_2的详情还没出，到记录这个的时候已经出了。。。

106 / 106 个通过测试用例
	状态：通过
执行用时：648 ms
内存消耗：16.7 MB
"""
