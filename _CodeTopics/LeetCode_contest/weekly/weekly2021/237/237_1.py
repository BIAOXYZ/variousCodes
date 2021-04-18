class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        ctr = collections.Counter(sentence)
        if len(ctr) == 26:
            return True
        return False
    
"""
https://leetcode-cn.com/submissions/detail/169126512/

79 / 79 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.3 MB
"""
