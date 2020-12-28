
# 2020.04.26

第 186 场周赛 https://leetcode-cn.com/contest/weekly-contest-186
- 5392. 分割字符串的最大得分 https://leetcode-cn.com/contest/weekly-contest-186/problems/maximum-score-after-splitting-a-string/
- 5393. 可获得的最大点数 https://leetcode-cn.com/contest/weekly-contest-186/problems/maximum-points-you-can-obtain-from-cards/
- 5394. 对角线遍历 II https://leetcode-cn.com/contest/weekly-contest-186/problems/diagonal-traverse-ii/
- 5180. 带限制的子序列和 https://leetcode-cn.com/contest/weekly-contest-186/problems/constrained-subset-sum/

# 笔记

## (2)

这题第一眼看觉得是队列，再看应该是贪心算法？反正因为被第一题给坑了，耽误了不少时间，最后没细想，直接奔第三题了。

## (3)

被第一题 + 环境（就上周我的vsvode调试python还没问题，今天一看只有python3了，还搞了一阵anaconda） + 工作上的事（下周三交代码）给烦的，第三题就写到这里了。回头补吧。

```py
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        length = len(nums)
        maxIndexSum = 2 * (length - 1)
        
        # 下标和还未超过length，此时全是从 [sum][0] 型的下标开始。
        for sum in range(length):
            for i in 
            
        for i in range(maxIndexSum):
            for j in range(min(maxIndexSum+1, length):
                print nums[j][maxIndexSum-j]
```
