class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        n = len(s)
        res = [n for _ in range(n)]
        for i in range(n):
            left = right = i
            while left >= 0 and s[left] != c:
                left -= 1
            if left >= 0 and s[left] == c:
                res[i] = min(res[i], i - left)
            while right <= n-1 and s[right] != c:
                right += 1
            if right <= n-1 and s[right] == c:
                res[i] = min(res[i], right - i)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/302179646/

执行用时：
72 ms
, 在所有 Python3 提交中击败了
23.24%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
19.48%
的用户
通过测试用例：
76 / 76
"""
