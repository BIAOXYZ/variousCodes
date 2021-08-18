class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        lis = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while left < len(s) and s[left] not in vowels:
                left += 1
            while right >= 0 and s[right] not in vowels:
                right -= 1
            if left < right:
                lis[left], lis[right] = lis[right], lis[left]
                left += 1
                right -= 1
            else:
                break
        return ''.join(lis)
        
"""
https://leetcode-cn.com/submissions/detail/208627200/

480 / 480 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 14.7 MB

执行用时：36 ms, 在所有 Python 提交中击败了98.25%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了55.56%的用户
"""
