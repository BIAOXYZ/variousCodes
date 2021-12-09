class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        dic = {}
        for ch in licensePlate:
            if ch.isalpha():
                dic[ch.lower()] = dic.setdefault(ch.lower(), 0) + 1

        def str_to_dict_v3(s):
            dic = {}
            for ch in s:
                dic[ch] = dic.get(ch, 0) + 1
            return dic
        
        minLen = 15
        res = ''
        for word in words:
            tmpDic = str_to_dict_v3(word)
            if all(tmpDic.get(k, 0) >= v for k, v in dic.items()) and len(word) < minLen:
                minLen = len(word)
                res = word
        return res
        
"""
https://leetcode-cn.com/submissions/detail/247030216/

执行用时：44 ms, 在所有 Python 提交中击败了47.06%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了5.88%的用户
通过测试用例：
102 / 102
"""
