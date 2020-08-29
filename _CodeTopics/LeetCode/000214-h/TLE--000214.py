class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        # 首先想到的idea是先把原字符串s直接补一半，补成一个回文，然后从后向前搜索，直到找到
        ## 最短的且包含s的第一个回文串。比如：
        ## "aacecaaa" 补成 "aaacecaa-aacecaaa"，然后从后向前查找到答案应该是"a-aacecaaa"

        # 但是这个有问题，比如"xxy"，其实只补一个"y"就行了，而不是补成"yxx-xxy"。
        ## 所以看起来应该是把s开头的最长回文子串排除掉，只从非回文的部分开始补。比如：
        ## "aacecaaa"排除掉开头最长的回文部分，只需要补一个"a"就行了。
        """

        def isPalindrome(s):
            if not s:
                return True
            length = len(s)
            left, right = 0, length - 1
            # 这里加不加等号都是一样的。
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        length = len(s)
        if length < 2:
            return s
        
        for i in range(length - 1, -1, -1):
            if not isPalindrome(s[:i+1]):
                continue
            else:
                if i == length - 1:
                    return s
                else:
                    tmp = s[i+1:]
                    tmp = tmp[::-1]
                    return tmp + s
                    
"""
https://leetcode-cn.com/submissions/detail/102923602/

119 / 120 个通过测试用例
状态：超出时间限制
"""
