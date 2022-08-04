class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        # 第 183 场周赛第一题（我是从第180场周赛开始的，快回到梦开始的地方了。。。）
        summ = sum(nums)
        nums.sort(reverse=True)
        i, currSum = 0, 0
        while currSum <= summ // 2:
            currSum += nums[i]
            i += 1
        return nums[:i]
        
"""
https://leetcode.cn/submissions/detail/345975652/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
65.45%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
18.18%
的用户
通过测试用例：
103 / 103
"""
