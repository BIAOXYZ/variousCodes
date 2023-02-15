class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        ctr = Counter(nums)
        return [
            sum(val // 2 for val in ctr.values()),
            sum(val % 2 for val in ctr.values())
        ]
        
"""
https://leetcode.cn/submissions/detail/402803673/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
19.60%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
27.64%
的用户
通过测试用例：
128 / 128
"""
