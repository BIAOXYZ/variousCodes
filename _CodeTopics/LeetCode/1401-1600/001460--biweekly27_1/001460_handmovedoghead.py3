class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        # 手动狗头题
        return sorted(target) == sorted(arr)
        
"""
https://leetcode.cn/submissions/detail/354131475/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
19.57%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
5.65%
的用户
通过测试用例：
106 / 106
"""
