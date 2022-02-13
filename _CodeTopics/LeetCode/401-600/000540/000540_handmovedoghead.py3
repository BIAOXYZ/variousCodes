class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # 手动狗头一把（但是不符合题目的复杂度要求）
        return [k for k, v in Counter(nums).items() if v == 1][0]
        
"""
https://leetcode-cn.com/submissions/detail/268015893/

执行用时：48 ms, 在所有 Python3 提交中击败了15.16%的用户
内存消耗：24.5 MB, 在所有 Python3 提交中击败了5.01%的用户
通过测试用例：
15 / 15
"""
