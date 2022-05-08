class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        n = len(s)
        small, large = 0, n
        res = []
        for i, ch in enumerate(s):
            if ch == 'D':
                res.append(large)
                large -= 1
            else:
                res.append(small)
                small += 1
        res.append(large) # 这里 append small 也是可以的，因为数据保证此时一定相等
        return res
        
"""
https://leetcode-cn.com/submissions/detail/311032188/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
65.52%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
27.85%
的用户
通过测试用例：
95 / 95
"""
