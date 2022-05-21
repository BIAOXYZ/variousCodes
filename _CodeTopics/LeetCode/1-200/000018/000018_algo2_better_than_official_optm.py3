class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # 类似 `000015_algo2_better_than_official_optm.py3`，加入了可选优化。
        
        n = len(nums)
        if n < 4:
            return []
        nums.sort()

        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 这两个 if 对应的优化是可选的，可以不加。
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # 同上，这两个 if 对应的优化也是可选的，可以不加。
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                left, right = j+1, n-1
                while left < right:
                    currSum = nums[i] + nums[j] + nums[left] + nums[right]
                    currArr = [nums[i], nums[j], nums[left], nums[right]]
                    if currSum == target:
                        if not res or currArr != res[-1]:
                            res.append(currArr)
                        left += 1
                        right -= 1
                    elif currSum < target:
                        left += 1
                    else:
                        right -= 1
        return res
        
"""
https://leetcode.cn/submissions/detail/316361520/

执行用时：
112 ms
, 在所有 Python3 提交中击败了
78.22%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
50.25%
的用户
通过测试用例：
289 / 289
"""
