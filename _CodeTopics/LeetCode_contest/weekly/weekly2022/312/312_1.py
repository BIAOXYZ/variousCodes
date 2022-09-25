class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        zipped = zip(names, heights)
        zipped.sort(key = lambda x : x[1], reverse=True)
        return [elem[0] for elem in zipped]
    
"""
https://leetcode.cn/submissions/detail/366892346/

68 / 68 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.4 MB
"""
