import random
class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dic[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

"""
https://leetcode-cn.com/submissions/detail/304980742/

执行用时：
104 ms
, 在所有 Python3 提交中击败了
30.87%
的用户
内存消耗：
25 MB
, 在所有 Python3 提交中击败了
13.91%
的用户
通过测试用例：
14 / 14
"""
