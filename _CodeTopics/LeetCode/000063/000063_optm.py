class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        """
        优化：还是用dp（这题除了dp也没有其他“比较常规的”解法了），但是参考官方答案中提到
        的「滚动数组思想」，降低空间复杂度。
        另外官方答案是申请了一个和列等长的数组（这个明显也更自然），但是这里准备申请一个和
        行等长的数组，换个方式实现这个优化。
        """

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [0 for i in range(rows)]

        # 代码能走到这儿就说明前面 obstacleGrid[0][0] 肯定不是1，也就是出发点没有障碍物。
        dp[0] = 1
        # 这里就要先从列开始循环了。
        for j in range(cols):
            for i in range(rows):
                if obstacleGrid[i][j] == 1:
                    # 这里还需要手动置0一下，而不能向上一个算法一样直接过去，因为上一个算法
                    # 初始化了二维的数组，默认值都已经是0了，但是这里只能靠这个一维数组。
                    dp[i] = 0
                    continue
                if i > 0 and obstacleGrid[i-1][j] != 1:
                    dp[i] += dp[i-1]       
        return dp[rows-1]
        
"""
https://leetcode-cn.com/submissions/detail/85229707/

41 / 41 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：12.6 MB
"""
"""
# 这空间优化了下和前面那个一模一样啊。。。时间也一样- -应该是差距太小体现不出来- -

执行用时：16 ms, 在所有 Python 提交中击败了92.23%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了16.67%的用户
"""
