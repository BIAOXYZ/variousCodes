class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        # 其实也可以申请长度为n+1的list，更符合自然逻辑。
        # 像我这种申请n长的数组的话，dp[i]其实表示的是有i+1个节点时共有多少种。
        dp = [0 for i in range(n)]
        dp[0], dp[1] = 1, 2

        for i in range(2,n):
            largestNodeNumber = i + 1
            for j in range(1, largestNodeNumber + 1):
                # 编号为j的点做root，左边有j-1个点，但是对于的dp值应该是dp[j-2]；右边也类似。
                number = dp[j-2] * dp[largestNodeNumber-j-1]
                dp[i] += number

        #// 写到这里就能发现，dp[j-2]，j=1的时候，应该是dp[-1]，可是dp[-1]其实是dp最后一个元素。
        #// 所以最终发现还是得申请n+1长的数组dp。
        #// 当然也不是完全没办法，比如再加个if分支，这样代码还是挺丑陋的，不过还是写完算了。
        """
        
        if n == 0: return 1
        elif n == 1: return 1
        elif n == 2: return 2

        dp = [0 for i in range(n)]
        dp[0], dp[1] = 1, 2

        for i in range(2,n):
            largestNodeNumber = i + 1
            for j in range(1, largestNodeNumber + 1):
                currnumber = 0
                if j == 1 or j == largestNodeNumber:
                    currnumber = dp[i-1]
                else:
                    currnumber = dp[j-2] * dp[largestNodeNumber-j-1]
                dp[i] += currnumber
        return dp[n-1]
        
"""
https://leetcode-cn.com/submissions/detail/88060966/

19 / 19 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：13 MB
"""
"""
执行用时：16 ms, 在所有 Python 提交中击败了82.74%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了33.33%的用户
"""
