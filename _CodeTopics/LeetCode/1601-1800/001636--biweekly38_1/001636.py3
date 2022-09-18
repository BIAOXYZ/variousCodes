class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        ctr = Counter(nums)
        keys = list(ctr.keys())
        keys.sort(key = lambda x : (ctr[x], -x))
        res = []
        for key in keys:
            for _ in range(ctr[key]):
                res.append(key)
        return res
        
"""
https://leetcode.cn/submissions/detail/364576819/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
78.21%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
12.82%
的用户
通过测试用例：
180 / 180
"""
