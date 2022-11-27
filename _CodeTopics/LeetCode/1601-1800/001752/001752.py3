class Solution:
    def check(self, nums: List[int]) -> bool:

        def rotated_list(lis, x):
            return [lis[(i-x) % (len(lis))] for i in range(len(lis))]

        n = len(nums)
        originallySorted = sorted(nums)
        for i in range(n):
            if rotated_list(originallySorted, i) == nums:
                return True
        return False
        
"""
https://leetcode.cn/submissions/detail/385255965/

执行用时：
52 ms
, 在所有 Python3 提交中击败了
7.50%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
78.75%
的用户
通过测试用例：
105 / 105
"""
