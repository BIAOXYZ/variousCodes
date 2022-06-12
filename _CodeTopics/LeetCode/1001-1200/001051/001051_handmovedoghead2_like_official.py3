class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        # 手动狗头题2 -- 参考官方答案，进一步用熟练 zip
        return sum(1 for x, y in zip(heights, sorted(heights)) if x != y)
        
"""
https://leetcode.cn/submissions/detail/324579150/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
49.36%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
94.90%
的用户
通过测试用例：
81 / 81
"""
