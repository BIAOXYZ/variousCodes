class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])
        # 怀疑上一个提交里这部分是不需要的（虽然又练了一次矩阵取列）。
        """
        if m == 1:
            return mat[0]
        elif n == 1:
            return list(zip(*mat))[0]
        """
        
        res = []
        i = j = 0
        flag = "upright"
        while i < m and j < n:
            res.append(mat[i][j])
            if flag == "upright":
                # 此时沿着右上移动，且既没有到第 0 行，也没有到第 n-1 列。
                if i > 0 and j < n - 1:
                    i -= 1
                    j += 1
                # 此时沿着右上移动，且到了第 0 行（也就是最顶端）。
                # 那么下一步应该是列往右移一步。
                elif i == 0 and j < n - 1:
                    j += 1
                    flag = "downleft"
                # 此时沿着右上移动，且到了第 n-1 列（也就是最右端）。
                # 那么下一步应该是行往下移一步。
                else:
                    i += 1
                    flag = "downleft"
            elif flag == "downleft":
                # 这里三处和上面三处对应，不再注释了。
                if j > 0 and i < m - 1:
                    i += 1
                    j -= 1
                elif j == 0 and i < m - 1:
                    i += 1
                    flag = "upright"
                else:
                    j += 1
                    flag = "upright"
        return res
        
"""
https://leetcode.cn/submissions/detail/324967880/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
74.92%
的用户
内存消耗：
17.1 MB
, 在所有 Python3 提交中击败了
40.72%
的用户
通过测试用例：
32 / 32
"""
