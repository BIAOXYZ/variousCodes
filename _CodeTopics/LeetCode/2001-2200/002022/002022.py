class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        length = len(original)
        if length != m * n:
            return []
        
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(length):
            row, col = i // n, i % n
            res[row][col] = original[i]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/253920723/

执行用时：112 ms, 在所有 Python3 提交中击败了26.49%的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了19.02%的用户
通过测试用例：
107 / 107
"""
"""
2022 年第一个提交，今天正式开始把刷题语言从 Python2 变成 Python3！ 
"""
