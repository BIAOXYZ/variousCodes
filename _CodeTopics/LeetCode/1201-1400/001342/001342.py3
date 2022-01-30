class Solution:
    def numberOfSteps(self, num: int) -> int:

        step = 0
        while num > 0:
            num = num - 1 if num & 1 == 1 else num // 2
            step += 1
        return step
        
"""
https://leetcode-cn.com/submissions/detail/263851554/

执行用时：36 ms, 在所有 Python3 提交中击败了40.48%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了59.52%的用户
通过测试用例：204 / 204
"""
