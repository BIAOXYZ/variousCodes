class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        n = len(word)
        slow, fast = 0, 0
        dic = {"a":1, "e":2, "i":3, "o":4, "u":5}
        flag = dic["a"]
        currLen = maxLen = 0
        while fast < n:
            if dic[word[slow]] != 1:
                slow += 1
                fast += 1
                continue
            if flag == 5 and dic[word[fast]] != 5:
                maxLen = max(maxLen, fast - slow)
                slow = fast
                fast += 1
                flag = 1
                continue
            if dic[word[fast]] == flag:
                fast += 1
                continue          
            if dic[word[fast]] == flag + 1:
                fast += 1
                flag += 1
                continue
            if abs(dic[word[fast]] - flag) > 1:
                slow = fast
                fast += 1
                flag = 1
        if flag == 5:
            maxLen = max(maxLen, fast - slow)
        return maxLen
    
"""
https://leetcode-cn.com/submissions/detail/171690376/

16 / 96 个通过测试用例
状态：超出时间限制

最后执行的输入：
"eiauouoaieoeaiuuoiaeeauioaiuoeiaoeueoiuaauioeeauoi"
"""
