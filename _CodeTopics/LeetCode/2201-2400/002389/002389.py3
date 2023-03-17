class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        prefixSum = list(itertools.accumulate(nums))
        res = []
        for query in queries:
            ind = bisect.bisect_right(prefixSum, query)
            res.append(ind)
        return res
        
"""
https://leetcode.cn/submissions/detail/414326150/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
80.61%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
26.02%
的用户
通过测试用例：
57 / 57
"""
