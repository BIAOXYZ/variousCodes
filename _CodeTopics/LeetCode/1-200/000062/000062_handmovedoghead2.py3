import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # 手动狗头题。
        # 注意，math.comb()只有python3有，python2没有。。。
        return math.comb(m + n - 2, m - 1)  # 或者 math.comb(m + n - 2, n - 1)，两个一样的。
        
"""
https://leetcode-cn.com/submissions/detail/129854363/

62 / 62 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.5 MB

执行用时：40 ms, 在所有 Python3 提交中击败了67.30%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了35.41%的用户
"""
