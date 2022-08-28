import itertools
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        # 手动狗头题
        return list(itertools.chain.from_iterable([(nums[i], nums[i+len(nums)//2]) for i in range(len(nums)//2)]))
        
"""
https://leetcode.cn/submissions/detail/356092710/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
54.95%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
5.66%
的用户
通过测试用例：
53 / 53
"""
