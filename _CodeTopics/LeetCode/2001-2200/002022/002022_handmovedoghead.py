class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        # 手动狗头题
        # from 官方答案
        return [original[i: i + n] for i in range(0, len(original), n)] if len(original) == m * n else []
        
"""
https://leetcode-cn.com/submissions/detail/253922343/

执行用时：52 ms, 在所有 Python3 提交中击败了98.64%的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了72.96%的用户
通过测试用例：
107 / 107
"""
