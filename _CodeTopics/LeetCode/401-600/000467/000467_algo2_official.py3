class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        # 参考官方答案，用 ch 结尾的最长连续串来统计，而不是用 ch 开头的。
        # 但是 ch 开头的应该也可以吧，可能只是写起来困难？回头写一下。

        dp = defaultdict(int)
        currLen = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                currLen += 1
            else:
                currLen = 1
            dp[ch] = max(dp[ch], currLen)
        return sum(dp.values())
        
"""
https://leetcode.cn/submissions/detail/317727776/

执行用时：
80 ms
, 在所有 Python3 提交中击败了
87.72%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
40.35%
的用户
通过测试用例：
81 / 81
"""
