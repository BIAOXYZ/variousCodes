class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # 手动狗头题
        return [num for num in nums if num & 1 == 0] + [num for num in nums if num & 1 == 1]
        
"""
https://leetcode-cn.com/submissions/detail/306408263/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
9.51%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
33.42%
的用户
通过测试用例：
285 / 285
"""
