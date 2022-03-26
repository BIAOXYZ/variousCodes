class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        # 官方答案。主要就是为了记录这个 `divmod`。
        missingSum = mean * (n + len(rolls)) - sum(rolls)
        if not n <= missingSum <= n * 6:
            return []
        quotient, remainder = divmod(missingSum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)
        
"""
https://leetcode-cn.com/submissions/detail/290001299/

执行用时：
76 ms
, 在所有 Python3 提交中击败了
86.42%
的用户
内存消耗：
19.6 MB
, 在所有 Python3 提交中击败了
23.46%
的用户
通过测试用例：
64 / 64
"""
