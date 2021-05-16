class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ctr = collections.Counter(s)
        if abs(ctr["0"] - ctr["1"]) >= 2:
            return -1
        
        res = 0
        n = len(s)
        if n % 2 == 0:
            for i in range(2, n, 2):
                if s[i] != s[0]:
                    res += 1
        else:
            if ctr["0"] > ctr["1"]:
                big = "0"
            else:
                big = "1"
            for i in range(0, n, 2):
                if s[i] != big:
                    res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/177908001/

15 / 124 个通过测试用例
状态：解答错误

最后执行的输入：
"1110000000100001010100101010000101010101001000001110101000010111101100000111110001000111010111101100001100001001100101011110100011111100000000100011111011110111111011110111010100111101011111111101101100101010110000011110110100101111000100000001100000"
"""
