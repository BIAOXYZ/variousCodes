class Solution:
    def digitCount(self, num: str) -> bool:
        
        n = len(num)
        ctr = Counter(num)
        for i, ch in enumerate(num):
            if ctr[str(i)] != int(ch):
                return False
        return True
    
"""
https://leetcode.cn/submissions/detail/319178335/

433 / 433 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 14.8 MB
"""
