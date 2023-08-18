class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        # 这个代码的整体思路是错误的，所以不能用。本来想着把整个数组划分成三个三个的块，每个块里选一个。
        # 但是第一个用例 [1,2,3,4,5,6] 就不行：因为最佳答案 4 和 6 总是在一个块里，按这种方式是选不到一起的。
        
        # 所以就是提交一下，记录下就算了，这个思路是死胡同，走不下去的。

        m = len(slices)
        n = m // 3

        dp = [[0 for _ in range(3)] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[0][0], dp[0][1], dp[0][2] = slices[0], slices[1], slices[2]
            elif i < n-1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + slices[3*i]
                dp[i][1] = max(dp[i-1]) + slices[3*i+1]
                dp[i][2] = max(dp[i-1]) + slices[3*i+2]
            elif i == n-1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + slices[3*i]
                dp[i][1] = max(dp[i-1]) + slices[3*i+1]

        dp2 = [[0 for _ in range(3)] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp2[0][1], dp2[0][2] = slices[1], slices[2]
            else:
                dp2[i][0] = max(dp2[i-1][0], dp2[i-1][1]) + slices[3*i]
                dp2[i][1] = max(dp2[i-1]) + slices[3*i+1]
                dp2[i][2] = max(dp2[i-1]) + slices[3*i+2]

        return max(max(dp[n-1]), max(dp2[n-1]))
        
"""
https://leetcode.cn/problems/pizza-with-3n-slices/submissions/457769868/
"""
