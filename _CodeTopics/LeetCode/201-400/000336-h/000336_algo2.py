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
            # 还不如把里面word[]里面的j相关的数组下标给改了。。。
            for j in range(wordlength+1):
                if j > 0 and isPalindrome(word[:j]):
                    if indexDic.has_key(word[j:wordlength]):
                        rightIndex = indexDic[word[j:wordlength]]
                        if rightIndex != i:
                            res.append([rightIndex, i])
                if isPalindrome(word[j:wordlength]):
                    if indexDic.has_key(word[:j]):
                        leftIndex = indexDic[word[:j]]
                        if leftIndex != i:
                            res.append([i, leftIndex])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/95435515/

134 / 134 个通过测试用例
状态：通过
执行用时：528 ms
内存消耗：14.3 MB
"""
"""
执行用时：528 ms, 在所有 Python 提交中击败了72.92%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了80.00%的用户
"""
