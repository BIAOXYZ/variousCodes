class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        n = len(nums)
        for i in range(n):
            while True:
                swapInd = nums[i] - 1
                if nums[i] != nums[swapInd]:
                    nums[swapInd], nums[i] = nums[i], nums[swapInd]
                else:
                    break
        return [num for i, num in enumerate(nums) if num != i + 1]
        
"""
https://leetcode-cn.com/submissions/detail/310614820/

执行用时：
112 ms
, 在所有 Python3 提交中击败了
25.64%
的用户
内存消耗：
21.1 MB
, 在所有 Python3 提交中击败了
86.20%
的用户
通过测试用例：
28 / 28
"""
