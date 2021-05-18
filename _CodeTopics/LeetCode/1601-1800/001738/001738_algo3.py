class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # 由于一维前缀和（`TLE--001738.py`）都不给力——想想就知道了，大致是1000的三次方也就是十亿的量级，所以超时也正常。
        # 所以改为用二维前缀和，这里实质其是动态规划，而且可以说是很regular的dp了。。。
        
        m, n = len(matrix), len(matrix[0])
        prefixXor = [[0 for _ in range(n)] for _ in range(m)]
        vals = []

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    prefixXor[i][j] = matrix[i][j]
                elif i == 0:
                    prefixXor[i][j] = prefixXor[i][j-1] ^ matrix[i][j]
                elif j == 0:
                    prefixXor[i][j] = prefixXor[i-1][j] ^ matrix[i][j]
                else:
                    prefixXor[i][j] = prefixXor[i][j-1] ^ prefixXor[i-1][j] ^ prefixXor[i-1][j-1] ^ matrix[i][j]
                vals.append(prefixXor[i][j])
        vals.sort(reverse=True)
        return vals[k-1]
        
"""
https://leetcode-cn.com/submissions/detail/178783117/

49 / 49 个通过测试用例
状态：通过
执行用时: 1008 ms
内存消耗: 43.1 MB

执行用时：1008 ms, 在所有 Python 提交中击败了64.71%的用户
内存消耗：43.1 MB, 在所有 Python 提交中击败了35.29%的用户
"""
