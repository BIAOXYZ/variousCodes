class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # 类似 `000015_algo2_better_than_official.py3`，算是总结了一个比官方答案不论
        # 读起来，还是写起来都更顺手的实现，以后偶尔复习的话就用这种写法。
        
        n = len(nums)
        if n < 4:
            return []
        nums.sort()

        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
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
https://leetcode.cn/submissions/detail/316352360/

执行用时：
1268 ms
, 在所有 Python3 提交中击败了
19.32%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
32.96%
的用户
通过测试用例：
289 / 289
"""
