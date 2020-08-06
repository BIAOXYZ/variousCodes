class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        """
        思想：暴力尝试。把所有可能的配对，一共是n(n-1)对，挨个组成字符串并放到判断
        是否是回文的子函数里。估计肯定是超时的。
        """

        def isPalindrome(s):
            length = len(s)
            left, right = 0, length-1
            # 这里加不加等号都是一样的。
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        length = len(words)
        indexArray = [[i,j] for i in range(length) for j in range(length)]
        res = []
        for index in indexArray:
            if index[0] == index[1]:
                continue
            s = words[index[0]] + words[index[1]]
            if isPalindrome(s):
                res.append(index)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/95282454/

94 / 134 个通过测试用例
状态：超出时间限制
"""
