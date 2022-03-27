class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        flag = 1 if n & 1 else 0
        n >>= 1
        while n > 0:
            if flag == n & 1:
                return False
            n >>= 1
            flag = flag ^ 1
        return True
        
"""
https://leetcode-cn.com/submissions/detail/290566250/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
32.89%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
45.61%
的用户
通过测试用例：
204 / 204
"""
