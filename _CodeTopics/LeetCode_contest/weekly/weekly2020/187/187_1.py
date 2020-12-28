class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        
        resdic = {}
        for path in paths:    
            resdic[path[0]] = 0
            if resdic.has_key(path[1]) is False:
                resdic[path[1]] = 1
        
        for k, v in resdic.items():
            if v == 1:
                return k
            
"""
103 / 103 个通过测试用例
	状态：通过
执行用时：24 ms
内存消耗：12.7 MB
"""
