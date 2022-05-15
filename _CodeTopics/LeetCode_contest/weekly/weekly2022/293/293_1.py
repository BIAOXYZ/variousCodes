class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        res = []
        for i in range(len(words)-1, 0, -1):
            cur, pre = words[i], words[i-1]
            if Counter(cur) == Counter(pre):
                continue
            else:
                res.append(cur)
        res.append(words[0])
        return list(reversed(res))
    
"""
https://leetcode.cn/submissions/detail/313647544/

201 / 201 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 13.3 MB
"""
