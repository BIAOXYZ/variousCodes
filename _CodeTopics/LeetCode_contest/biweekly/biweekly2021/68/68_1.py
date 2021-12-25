class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
        res = 0
        for s in sentences:
            res = max(res, len(s.split()))
        return res
    
"""
https://leetcode-cn.com/submissions/detail/252008973/

90 / 90 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
