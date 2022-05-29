class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        ctr1 = Counter(s)
        ctr2 = Counter(target)
        return min(ctr1[k] // ctr2[k] for k in ctr2.keys())
    
"""
https://leetcode.cn/submissions/detail/319295358/

113 / 113 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15 MB
"""
