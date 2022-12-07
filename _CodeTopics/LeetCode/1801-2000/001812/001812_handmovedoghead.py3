class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        # 手动狗头题
        return (int(coordinates[1]) + (ord(coordinates[0]) - ord('a') + 1)) % 2 == 1
        
"""
https://leetcode.cn/submissions/detail/387773430/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
90.50%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
6.61%
的用户
通过测试用例：
64 / 64
"""
