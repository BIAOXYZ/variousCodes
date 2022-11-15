class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:

        n = len(nums)
        prefixMinReverseOrder = [None for _ in range(n)]
        currMin = n - 1
        for i in range(n-1, -1, -1):
            currMin = min(currMin, nums[i])
            prefixMinReverseOrder[i] = currMin
        for i in range(n-2):
            if nums[i] > prefixMinReverseOrder[i+2]:
                return False
        return True
        
"""
https://leetcode.cn/submissions/detail/382358556/

执行用时：
208 ms
, 在所有 Python3 提交中击败了
25.00%
的用户
内存消耗：
25.3 MB
, 在所有 Python3 提交中击败了
43.18%
的用户
通过测试用例：
226 / 226
"""
