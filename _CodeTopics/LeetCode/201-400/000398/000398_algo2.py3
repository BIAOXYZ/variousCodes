import random
class Solution:

    # 蓄水池抽样/水塘抽样。官方答案不太注意细节，这里自己写一个更好复习的版本。

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = -1
        totalNumOfTarget = 0
        for ind, num in enumerate(self.nums):
            if num == target:
                totalNumOfTarget += 1
                # 第一次肯定会等于 0，对应了如果 target 只有一个的话，肯定能抽到
                if random.randrange(totalNumOfTarget) == 0:
                    res = ind
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

"""
https://leetcode-cn.com/submissions/detail/304993960/

执行用时：
76 ms
, 在所有 Python3 提交中击败了
88.44%
的用户
内存消耗：
18.3 MB
, 在所有 Python3 提交中击败了
68.74%
的用户
通过测试用例：
14 / 14
"""
