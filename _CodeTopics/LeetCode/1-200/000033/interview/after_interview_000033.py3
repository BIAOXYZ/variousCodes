class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0, n-1
        found = False
        res = None

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                found = True
                res = mid
                break
            elif nums[mid] >= nums[0]:
                if target < nums[mid] and target >= nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
            # nums[mid] > target
            elif nums[mid] < nums[0]:
                if target > nums[mid] and target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        if found:
            print("res is: ", res)
            return res
        else:
            print("res is: ", -1)
            return -1
        
"""
https://leetcode.cn/submissions/detail/320442719/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
73.39%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
62.74%
的用户
通过测试用例：
195 / 195
"""
