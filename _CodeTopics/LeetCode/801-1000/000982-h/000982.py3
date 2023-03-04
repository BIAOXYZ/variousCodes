class Solution:
    def countTriplets(self, nums: List[int]) -> int:

        ctr = Counter([num1 & num2 for num1 in nums for num2 in nums])
        res = 0
        for num in nums:
            for val, freq in ctr.items():
                if num & val == 0:
                    res += freq
        return res
        
"""
https://leetcode.cn/submissions/detail/409022367/

执行用时：
3500 ms
, 在所有 Python3 提交中击败了
31.37%
的用户
内存消耗：
52.1 MB
, 在所有 Python3 提交中击败了
5.88%
的用户
通过测试用例：
25 / 25
"""
