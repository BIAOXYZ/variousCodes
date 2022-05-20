class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        # 手动狗头题
        ctr = Counter(nums)
        return list( filter(lambda k : ctr[k] > 1, ctr.keys()) )[0]
        
"""
https://leetcode.cn/submissions/detail/316125313/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
35.25%
的用户
内存消耗：
16.2 MB
, 在所有 Python3 提交中击败了
16.82%
的用户
通过测试用例：
102 / 102
"""
"""
（对比 `TLE--000961_handmovedoghead.py3` ）为什么 Python 的优化这么差。。。
"""
