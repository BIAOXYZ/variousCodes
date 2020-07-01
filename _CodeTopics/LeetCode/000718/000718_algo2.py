class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        """
        思想：
        朴素的穷举遍历即使加上优化也不行，那就先动态规划试试吧。
        """

        lena, lenb = len(A), len(B)
        dp = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]

        maxlongest = 0
        """
        # 注意，因为申请时候多申请了一层，所以这里range内部还是从lena-1或lenb-1开始，不用担心
        # 下面dp[i+1][j+1]下标超出范围。举个具体的例子：A:[1,2,3] B:[4,5]。那么dp其实就是：
        [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]
        # 位置填一下会发现恰好多了1行1列，所以任何dp[i+i][xxx]或dp[xxx][j+1]都不会超出下标：
        [[dp00, dp01, 0], 
         [dp10, dp11, 0], 
         [dp20, dp21, 0], 
         [0,    0,    0]]
        """
        for i in range(lena-1,-1,-1):
            for j in range(lenb-1,-1,-1):
                if A[i] != B[j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j+1] + 1
                maxlongest = max(maxlongest, dp[i][j])
        return maxlongest
        
"""
https://leetcode-cn.com/submissions/detail/83776790/

54 / 54 个通过测试用例
状态：通过
执行用时：3964 ms
内存消耗：34.5 MB
"""
