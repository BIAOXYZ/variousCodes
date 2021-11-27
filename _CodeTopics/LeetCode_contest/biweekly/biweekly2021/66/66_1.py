class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        
        ctr1 = collections.Counter(words1)
        ctr2 = collections.Counter(words2)
        res = 0
        for k, v in ctr1.items():
            if v == 1 and ctr2.get(k, 0) == 1:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/242920420/

60 / 60 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.6 MB
"""
