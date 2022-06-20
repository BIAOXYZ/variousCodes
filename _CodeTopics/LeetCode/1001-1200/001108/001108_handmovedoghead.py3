class Solution:
    def defangIPaddr(self, address: str) -> str:

        # 手动狗头题
        return address.replace('.', '[.]')
        
"""
https://leetcode.cn/submissions/detail/327459226/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
67.98%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
通过测试用例：
62 / 62
"""
