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
https://leetcode-cn.com/submissions/detail/208626973/

10 / 480 个通过测试用例
状态：执行出错
提交时间：几秒前
执行出错信息：
IndexError: string index out of range
    while s[left] not in vowels:
Line 12 in reverseVowels (Solution.py)
    ret = Solution().reverseVowels(param_1)
Line 44 in _driver (Solution.py)
    _driver()
Line 54 in <module> (Solution.py)
最后执行的输入：
".,"
"""
