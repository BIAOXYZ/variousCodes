class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        ctr = Counter(words)
        maxSymm = 0
        res = 0
        for num1 in range(ord('a'), ord('z')+1):
            key = chr(num1)*2
            if key in ctr:
                maxSymm = max(maxSymm, ctr[key] * 2)
            for num2 in range(num1 + 1, ord('z')+1):
                key1, key2 = chr(num1) + chr(num2), chr(num2) + chr(num1)
                if key1 in ctr and key2 in ctr:
                    res += min(ctr[key1], ctr[key2]) * 4
        return res + maxSymm
    
"""
https://leetcode-cn.com/submissions/detail/256392274/

33 / 120 个通过测试用例
状态：解答错误

输入：
["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
输出：
10
预期：
22
"""
