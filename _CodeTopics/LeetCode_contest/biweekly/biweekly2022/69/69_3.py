class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        ctr = Counter(words)
        symmlis = []
        res = 0
        for num1 in range(ord('a'), ord('z')+1):
            key = chr(num1)*2
            if key in ctr:
                symmlis.append(ctr[key])
            for num2 in range(num1 + 1, ord('z')+1):
                key1, key2 = chr(num1) + chr(num2), chr(num2) + chr(num1)
                if key1 in ctr and key2 in ctr:
                    res += min(ctr[key1], ctr[key2]) * 4
        
        symmlis.sort(reverse=True)
        onlyBiggestOdd = False
        for elem in symmlis:
            if elem % 2 == 0:
                res += elem * 2
            else:
                onlyBiggestOdd = True
                res += (elem - 1) * 2
        return res + 2 if onlyBiggestOdd else res
    
"""
https://leetcode-cn.com/submissions/detail/256396145/

120 / 120 个通过测试用例
状态：通过
执行用时: 288 ms
内存消耗: 28.8 MB
"""
