class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        if n < 3:
            return []
        nums.sort()

        target = 0
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 这两个 if 对应的优化是可选的，可以不加。
            if nums[i] + nums[i+1] + nums[i+2] > target:
                break
            if nums[i] + nums[n-2] + nums[n-1] < target:
                continue
            # 官方答案的写法实在是不够清晰：第一重 for 循环之后，其实就是一个典型的双指针场景。
            # 但是官方答案非得把左指针 left 搞成一个 for 循环，就很别扭。。。我觉得我这个写法更清晰。
            # 并且应该也是类似的，能适用于四数之和的。
            left, right = i+1, n-1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                currArr = [nums[i], nums[left], nums[right]]
                if currSum == target:
                    # 这里如果 currArr 有可能是重复的，那只可能和 res 里最后一个元素是重复的。
                    # 当然也可以把 res 搞成 set，然后 currArr 搞成 tuple，用 set 的 add 来无脑添加，
                    ## 然后最后统一处理一下 res。但是没有必要，只要利用好题目的特点，就不需要用 set。
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
https://leetcode.cn/submissions/detail/316359152/

执行用时：
696 ms
, 在所有 Python3 提交中击败了
59.54%
的用户
内存消耗：
17.8 MB
, 在所有 Python3 提交中击败了
74.74%
的用户
通过测试用例：
318 / 318
"""
