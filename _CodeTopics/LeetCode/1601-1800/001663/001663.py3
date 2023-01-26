class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        res = []
        while n > 0:
            if (n-1) * 26 == k - 1:
                return ''.join(res) + 'a' + (n-1) * 'z'
            elif (n-1) * 26 > k - 1:
                res.append('a')
                n -= 1
                k -= 1
            else:
                ch = chr(ord('a') - 1 + k - (n-1) * 26)
                return ''.join(res) + ch + (n-1) * 'z'
        
"""
https://leetcode.cn/submissions/detail/397255779/

执行用时：
440 ms
, 在所有 Python3 提交中击败了
33.71%
的用户
内存消耗：
17 MB
, 在所有 Python3 提交中击败了
24.72%
的用户
通过测试用例：
94 / 94
"""
