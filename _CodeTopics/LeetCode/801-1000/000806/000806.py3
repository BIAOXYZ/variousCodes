class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        n = len(s)
        res, currLeftUnits = 1, 100
        i = 0
        while i < n:
            needed = widths[ord(s[i]) - ord('a')]
            if needed <= currLeftUnits:
                currLeftUnits -= needed
            else:
                res += 1
                currLeftUnits = 100 - needed
            i += 1
        return [res, 100-currLeftUnits]
        
"""
https://leetcode-cn.com/submissions/detail/298632773/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
90.64%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
85.67%
的用户
通过测试用例：
27 / 27
"""
