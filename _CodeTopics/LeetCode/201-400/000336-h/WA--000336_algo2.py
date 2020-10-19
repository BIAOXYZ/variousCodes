class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
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
        indexDic = {word[::-1]:i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            wordlength = len(word)
            # 这里要加2是因为要保证j的最大值减一后还能让整个word被word[:j-1]取到。
            for j in range(wordlength+2):
                if j > 0 and isPalindrome(word[:j-1]):
                    if indexDic.has_key(word[j:wordlength]):
                        rightIndex = indexDic[word[j:wordlength]]
                        if rightIndex != i:
                            res.append([rightIndex, i])
                if isPalindrome(word[j:wordlength]):
                    if indexDic.has_key(word[:j-1]):
                        leftIndex = indexDic[word[:j-1]]
                        if leftIndex != i:
                            res.append([i, leftIndex])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/95430907/

16 / 134 个通过测试用例
状态：解答错误

输入：["a",""]
输出：[[0,1],[1,0],[0,1],[1,0]]
预期：[[0,1],[1,0]]
"""
