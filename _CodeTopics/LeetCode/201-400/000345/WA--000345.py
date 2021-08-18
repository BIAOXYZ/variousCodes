class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        lis = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while s[left] not in vowels:
                left += 1
            while s[right] not in vowels:
                right -= 1
            if left < right:
                lis[left], lis[right] = lis[right], lis[left]
                left += 1
                right -= 1
            else:
                break
        return ''.join(lis)
        
"""
https://leetcode-cn.com/submissions/detail/208626595/

7 / 480 个通过测试用例
状态：解答错误

最后执行的输入：
"aA"
输出：
"aA"
预期结果：
"Aa"
"""
