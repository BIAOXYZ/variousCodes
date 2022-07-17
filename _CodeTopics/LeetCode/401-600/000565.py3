class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        globallyVisitedIndex = set()
        lis = []
        for i, num in enumerate(nums):
            if i not in globallyVisitedIndex:
                se = set([i])
                while nums[i] not in se:
                    se.add(nums[i])
                    i = nums[i]
                lis.append(se)
                globallyVisitedIndex |= se
        return len(max(lis, key=len))
        
"""
https://leetcode.cn/submissions/detail/338223722/

执行用时：
176 ms
, 在所有 Python3 提交中击败了
76.86%
的用户
内存消耗：
35 MB
, 在所有 Python3 提交中击败了
30.56%
的用户
通过测试用例：
885 / 885
"""
