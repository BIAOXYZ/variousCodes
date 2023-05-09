class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        se = set()
        remainder = 1
        while len(se) < k:
            if remainder % k == 0:
                return len(se) + 1
            if remainder in se:
                return -1
            else:
                se.add(remainder)
            remainder = (remainder * 10 + 1) % k
        
"""
https://leetcode.cn/submissions/detail/431211333/

执行用时：
52 ms
, 在所有 Python3 提交中击败了
62.34%
的用户
内存消耗：
20.2 MB
, 在所有 Python3 提交中击败了
5.19%
的用户
通过测试用例：
70 / 70
"""
