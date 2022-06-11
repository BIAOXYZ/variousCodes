class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        
        ddic = defaultdict(set)
        for old, new in mappings:
            ddic[old].add(new)
        
        def can_match_after_replace(s1, s2):
            n = len(s1)
            for i in range(n):
                if s1[i] != s2[i]:
                    if s1[i] not in ddic[s2[i]]:
                        return False
            return True
        
        n, m = len(s), len(sub)
        for i in range(n-m+1):
            if can_match_after_replace(s[i:i+m], sub):
                return True
        return False
    
"""
https://leetcode.cn/submissions/detail/324226850/

109 / 109 个通过测试用例
状态：通过
执行用时: 2604 ms
内存消耗: 13.6 MB
"""
