class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 两个都得最高评分1000，并且两个距离最短只有1，也就是1000*2-1。
        possibleMaxPoint = 1999

        # 距离一旦超过2000就没意义了，整体得分就会变成负值。所以其实就是大循环是
        # 输入数组的长度级别，小循环是固定的循环2000次。
        length = len(A)
        if length == 2:
            return A[0] + A[1] - 1

        currMaxPoint = 1
        for i in range(length):
            end = min(i+2000,length)
            for j in range(i+1,end):
                currMaxPoint = max(currMaxPoint, A[i]+A[j]+i-j)
        return currMaxPoint
        
"""
https://leetcode-cn.com/submissions/detail/79775887/

46 / 52 个通过测试用例
状态：超出时间限制

最后执行的输入：[402,224,922,720,323,714,129,303,556,532,925,824,466,169,725,83,647,908,624,342,425,757,25,770,468,402,537,891,94...
"""
