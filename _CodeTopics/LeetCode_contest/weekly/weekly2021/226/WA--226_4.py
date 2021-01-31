class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # 这写法不TLE才怪。。。不过不管了，先提一个- -
        
        def is_palindrome(s):
            length = len(s)
            left, right = 0, length-1
            # 这里加不加等号都是一样的。
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        length = len(s)
        for i in range(1, length-2):
            for j in range(i, length):
                if is_palindrome(s[:i]) and is_palindrome(s[i:j]) and is_palindrome(s[j:]):
                    return True
        return False
    
"""
https://leetcode-cn.com/submissions/detail/142505608/

74 / 81 个通过测试用例
状态：解答错误

输入：
"aaa"
输出：
false
预期：
true
"""
